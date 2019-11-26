# Standard Library
import os

# Third party
import bs4
from django.utils.translation import gettext as _

# Local application / specific library imports
from ..checks import custom_list


def importance():
    """Scripts with higher importance will be executed in first.

    Returns:
        int -- Importance of the script.
    """
    return 1


def run(site):
    """Check all link-related conditions
    """

    not_enough_internal = custom_list.CustomList(
        name=_("Not enough internal links"),
        settings=_("at least {}").format(site.settings.SEO_SETTINGS["internal_links"]),
        description=_(
            "Internal links are useful because they can give the structure of your website to search engines, so they can create a hierarchy of your pages."
        ),
    )

    enough_internal = custom_list.CustomList(
        name=_("Internal links were found"),
        settings=_("at least {}").format(site.settings.SEO_SETTINGS["internal_links"]),
        description=not_enough_internal.description,
    )

    not_enough_external = custom_list.CustomList(
        name=_("Not enough external links"),
        settings=_("at least {}").format(site.settings.SEO_SETTINGS["external_links"]),
        description=_(
            "External links help your users to check your topic and can save them from having to do additional research."
        ),
    )

    enough_external = custom_list.CustomList(
        name=_("External links were found"),
        settings=_("at least {}").format(site.settings.SEO_SETTINGS["external_links"]),
        description=not_enough_external.description,
    )

    links = bs4.element.ResultSet(None)

    # only get links with href
    for c in site.content:
        links += c.find_all("a", href=True)

    internal_links = 0
    external_links = 0

    for link in links:
        # internal links = absolute links that contains domain name or relative links
        if os.environ["DOMAIN_NAME"] in link["href"] or not link["href"].startswith(
            "http"
        ):
            internal_links += 1
        else:
            external_links += 1

    # not enough internal links
    if internal_links < site.settings.SEO_SETTINGS["internal_links"]:
        not_enough_internal.found = internal_links
        site.warnings.append(not_enough_internal)
    else:
        enough_internal.found = internal_links
        site.success.append(enough_internal)

    # not enough external links
    if external_links < site.settings.SEO_SETTINGS["external_links"]:
        not_enough_external.found = external_links
        site.warnings.append(not_enough_external)
    else:
        enough_external.found = external_links
        site.success.append(enough_external)
