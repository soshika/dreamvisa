from django.contrib import admin
from .models import Visa


class VisaAdmin(admin.ModelAdmin):
    fields = ['title', 'image', 'summary', 'description']
    list_display = ['title', 'image', 'summary', 'description']
    search_fields = ['title', 'summary', 'description']


admin.site.register(Visa, VisaAdmin)

