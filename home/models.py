from django.db import models
from wagtail.core import blocks
from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.embeds.blocks import EmbedBlock
from wagtail.images.blocks import ImageChooserBlock
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.admin.edit_handlers import StreamFieldPanel

class HomePage(Page):
    pass

class ArticlePage(Page):

    class Meta:
        verbose_name = "Standard Article"

    intro = models.TextField()

    body = StreamField([
        ('paragraph', blocks.RichTextBlock(icon="pilcrow")),
        ('html', blocks.RawHTMLBlock()),
        ('table', blocks.RawHTMLBlock()),
        ('image', ImageChooserBlock()),
        ('embed', EmbedBlock(icon="media")),
    ])

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full"),
        StreamFieldPanel('body'),
    ]