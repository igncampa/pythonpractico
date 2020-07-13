from django.db import models
from wagtail.core import blocks
from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.embeds.blocks import EmbedBlock
from wagtail.images.blocks import ImageChooserBlock
from wagtail.admin.edit_handlers import StreamFieldPanel

class HomePage(Page):
    pass

class ArticlePage(Page):

    class Meta:
        verbose_name = "Standard Article"

    body = StreamField([
        ('html', blocks.RawHTMLBlock()),
        ('image', ImageChooserBlock()),
        ('embed', EmbedBlock(
            icon="media",
        )),
        ('paragraph', blocks.RichTextBlock(
            icon="pilcrow"
        )),
    ])

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]