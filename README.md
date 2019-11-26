![Django Check SEO](https://user-images.githubusercontent.com/45763865/69130297-8def1800-0ab0-11ea-8e3f-973e0f97a080.png)

Replacing some features of Yoast or SEMrush for django CMS users.

In other words, django-check-seo will tell you if you have problems concerning a broad range of SEO aspects of your pages.

----

## Install

#### With pipenv

 * Add `django-check-seo = { git = 'https://github.com/kapt-labs/django-check-seo.git' }` to your Pipfile below `[packages]`, then run `pipenv install`,

**or**

 * Execute `pipenv install git+https://github.com/kapt-labs/django-check-seo#egg=django-check-seo` in your working directory,

**and then**

 * add `django-check-seo.apps.DjangoCheckSEOConfig` to your `INSTALLED_APPS`,
 * add the file [`cms_toolbars.py`](https://gist.githubusercontent.com/corentinbettiol/f1e4b6630b7ae9afe2f9023b2185f3db/raw/d8295436b105da966346cf754e51671f65409491/cms_toolbars.py) inside your `django_project_name` folder (at the same level as `settings.py` and `urls.py`),
 * add `url(r"^django-check-seo/", include("django-check-seo.urls")),` to your `urlpatterns` in `urls.py` (before `url(r'^', include('cms.urls')),` or it will not work),
 * (*optional*) export `DOMAIN_NAME` (used in the application), or put it inside your [`.env`](https://gist.github.com/corentinbettiol/f1e4b6630b7ae9afe2f9023b2185f3db#file-env) file

*Start your django CMS project, log in, you should see the "Check SEO..." button and everything should be okay.*

#### Without pipenv

*coming soon* 📝

----

## Prerequisites

You will need `djangocms` & `djangocms_page_meta` in order to made this application work.

----

## Want a screenshot?

![screenshot](https://user-images.githubusercontent.com/45763865/69637530-180f2180-1059-11ea-9d90-53ecf3b6c53b.png)

*Other screenshots and videos are available on the [wiki](https://github.com/kapt-labs/django-check-seo/wiki/Medias).*

----

## Interested in finding out more?

Take a look at the [wiki](https://github.com/kapt-labs/django-check-seo/wiki/):

 * [List & explanations of all checks](https://github.com/kapt-labs/django-check-seo/wiki/Description-of-the-checks)
 * [How to add a check?](https://github.com/kapt-labs/django-check-seo/wiki/How-to-add-a-check%3F)
 * ...
