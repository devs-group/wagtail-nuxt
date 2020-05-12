from django.db import models
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.fields import RichTextField
from wagtail.core.models import Page
from wagtail.images.edit_handlers import ImageChooserPanel


class InfoCard(models.Model):
    title = models.CharField(max_length=254)
    info = RichTextField(blank=True)
    image = models.ForeignKey('wagtailimages.Image', on_delete=models.SET_NULL,
                              verbose_name='Image', related_name='+',
                              null=True, blank=True)

    panels = [
        FieldPanel('title'),
        FieldPanel('info', classname='full'),
        ImageChooserPanel('image')
    ]

    def __str__(self):
        return self.title
