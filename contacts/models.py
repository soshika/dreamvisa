from django.db import models
from django.utils.translation import ugettext_lazy as _


class Contact(models.Model):
    name = models.CharField(max_length=255, verbose_name=_('Name'))
    phone = models.CharField(max_length=15, verbose_name=_('Phone'))
    email = models.EmailField(verbose_name=_('Email'))
    subject = models.CharField(max_length=255, verbose_name=_('Subject'))
    message = models.TextField(verbose_name=_('Message'))

    def __str__(self):
        return '{} - {}'.format(self.name, self.email)

    class Meta:
        verbose_name = _('Contact')
        verbose_name_plural = _('Contacts')
