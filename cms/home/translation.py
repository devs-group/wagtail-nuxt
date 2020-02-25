# COOKIECUTTER_PLACEHOLDER_TRANSLATIONS


# If we are getting error while starting the project. Please read following issue https://github.com/infoportugal/wagtail-modeltranslation/issues/196


from .models import (
    HomePage
)
from modeltranslation.translator import TranslationOptions
from modeltranslation.decorators import register


@register(HomePage)
class HomePageTR(TranslationOptions):
    fields = (
        'body',
    )
