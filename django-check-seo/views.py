# Standard Library
import json
import os

# Third party
from bs4 import BeautifulSoup
from django.utils.translation import gettext as _, ngettext
from django.views import generic
import requests

# Local application / specific library imports
from .checks import site
from .checks_list import launch_checks
from .conf import settings


class IndexView(generic.base.TemplateView):
    template_name = "default.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        # get http content of the page

        if "http" not in self.request.GET.get("page", None):
            full_url = (
                "http://"
                + os.environ["DOMAIN_NAME"]
                + self.request.GET.get("page", None)
            )
        else:
            full_url = self.request.GET.get("page", None)

        # do not get cached page (useful ?)
        r = requests.get(full_url, headers={"Cache-Control": "no-cache"})

        soup = BeautifulSoup(r.text, features="lxml")

        # populate class with data
        page_stats = site.Site(soup, full_url)

        # magic happens here!
        launch_checks.launch_checks(page_stats)

        (context["problems"], context["warnings"], context["success"]) = (
            page_stats.problems,
            page_stats.warnings,
            page_stats.success,
        )

        context["settings"] = json.dumps(settings.SEO_SETTINGS, indent=4)
        context["html"] = page_stats.content
        context["text"] = page_stats.content_text

        nb_problems = len(context["problems"])
        nb_warnings = len(context["warnings"])

        # define some fancy-looking text here because it is wayyy to dirty with all the {% trans %} in template
        if nb_problems == 0 and nb_warnings == 0:
            context["nb_problems_warnings"] = _(
                '<strong class="green-bg">No problem</strong> was found on the page!'
            )
        else:
            if nb_problems == 0:
                context["nb_problems_warnings"] = _(
                    '<strong class="green-bg">No problem</strong> found, and '
                )
            else:
                context["nb_problems_warnings"] = '<strong class="red-bg">'
                context["nb_problems_warnings"] += ngettext(
                    "{nb_problems} problem</strong> found, and ",
                    "{nb_problems} problems</strong> found, and ",
                    nb_problems,
                ).format(nb_problems=nb_problems)

            if nb_warnings == 0:
                context["nb_problems_warnings"] += _(
                    '<strong class="green-bg">no warning</strong> raised'
                )
            else:
                context["nb_problems_warnings"] += '<strong class="yellow-bg">'
                context["nb_problems_warnings"] += ngettext(
                    "{nb_warnings} warning</strong> raised",
                    "{nb_warnings} warnings</strong> raised",
                    nb_warnings,
                ).format(nb_warnings=nb_warnings)

        return context
