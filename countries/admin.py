from django.contrib import admin
from .models import Country


class CountryAdmin(admin.ModelAdmin):
    fields = ['country', 'summary', 'image', 'description']
    list_display = ['country', 'summary', 'description']
    search_fields = ['country']


admin.site.register(Country, CountryAdmin)
