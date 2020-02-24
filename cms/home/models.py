from django.http import HttpResponseRedirect
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.core.fields import RichTextField
from wagtail.core.models import Page


class TestPage(Page):
    body = RichTextField(blank=True, max_length=254)

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('body', classname="full")
        ], heading="COOKIECUTTER_PLACEHOLDER_WELCOME_TXT")
    ]

    def serve(self, request, *args, **kwargs):
        return HttpResponseRedirect('/admin/')
