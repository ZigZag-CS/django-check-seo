# Third party
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
    """Count number of words in content.
    """

    short_content = custom_list.CustomList(
        name=_("Content is too short"),
        settings=_("at least {min} words, more than {min2} if possible").format(
            min=site.settings.SEO_SETTINGS["content_words_number"][0],
            min2=site.settings.SEO_SETTINGS["content_words_number"][1],
        ),
        description=_(
            "Longer articles tend to be better ranked, but will require better writing skills than shorter articles."
        ),
    )

    nb_words = len(site.content_text.split())
    short_content.found = nb_words

    # too few words
    if nb_words < site.settings.SEO_SETTINGS["content_words_number"][0]:
        site.problems.append(short_content)

    elif nb_words < site.settings.SEO_SETTINGS["content_words_number"][1]:
        site.warnings.append(short_content)

    else:
        short_content.name = _("Content length is right")
        site.success.append(short_content)
