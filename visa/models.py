from django.db import models
from django.utils.translation import ugettext_lazy as _

from tinymce import HTMLField

# Create your models here.


class Visa(models.Model):
    image = models.ImageField(upload_to='images/', verbose_name=_('Image'))
    title = models.CharField(max_length=255, verbose_name=_('Title'))
    summary = models.CharField(max_length=255, verbose_name=_('Summary'))
    description = HTMLField('Content')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Visa')
        verbose_name_plural = _('Visas')


