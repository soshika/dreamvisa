from django.db import models
from tinymce import HTMLField
from jalali_date import datetime2jalali
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.


@python_2_unicode_compatible
class BlogManager(models.Manager):
    def get_queryset(self):
        return super(BlogManager, self).get_queryset().order_by('-id')

    def get_blogs(self):
        return self.get_queryset().order_by('-id')


class Blog(models.Model):
    title = models.CharField(max_length=255, verbose_name=_('Title'))
    summary = models.CharField(max_length=255, default='', verbose_name=_('Summary'))
    body = HTMLField('Content')
    image = models.ImageField(upload_to='images/', verbose_name=_('Image'))
    pub_date = models.DateTimeField(verbose_name=_('PublicDate'))

    objects = BlogManager()

    def __str__(self):
        return self.title

    def pub_date_pretty(self):
        return datetime2jalali(self.pub_date).strftime(settings.JALALI_FORMAT)

    class Meta:
        verbose_name = _('Blog')
        verbose_name_plural = _('Blogs')

#
# class Comment(models.Model):
#     name = models.CharField(max_length=127)
#     email = models.EmailField()
#     comment = models.TextField()
#     blog = models.ManyToManyField(Blog)
#     pub_date = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return '{}-{}'.format(self.name, self.email)
