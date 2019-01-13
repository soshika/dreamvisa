from django.db import models
from django.utils.translation import ugettext_lazy as _

from tinymce import HTMLField


class Country(models.Model):
    country = models.CharField(max_length=255)
    image = models.FileField(upload_to='images/countries/', verbose_name=_('Image'), default=None)
    summary = models.CharField(max_length=255, verbose_name=_('Summary'), default='')
    description = HTMLField('Content')

    def __str__(self):
        return self.country

    class Meta:
        verbose_name = _('Country')
        verbose_name_plural = _('Countries')
