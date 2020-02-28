from django.db import models
from modelcluster.models import ClusterableModel
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.core.fields import RichTextField
from wagtail.core.models import Page
from wagtail.images.edit_handlers import ImageChooserPanel


class HomePage(Page):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        # MultiFieldPanel allows grouping of multilang fields in admin
        MultiFieldPanel([
            FieldPanel('body', classname="full"),
        ], heading="Beschreibung")
    ]


class InfoCard(ClusterableModel):
    title = models.CharField(max_length=254)
    info = RichTextField(blank=True)
    image = models.ForeignKey('wagtailimages.Image', on_delete=models.SET_NULL,
                              verbose_name='Bild', related_name='+',
                              null=True, blank=True)

    panels = [
        MultiFieldPanel([
            FieldPanel('title')
        ]),
        MultiFieldPanel([
            FieldPanel('info', classname='full')
        ], heading="info"),
        ImageChooserPanel('image')
    ]

    def __str__(self):
        return self.title
