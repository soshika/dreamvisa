from django.contrib import admin
from .models import Country


class CountryAdmin(admin.ModelAdmin):
    fields = ['country', 'summary', 'image', 'flag_image', 'description']
    list_display = ['country', 'summary', 'image', 'flag_image', 'description']
    search_fields = ['country']


admin.site.register(Country, CountryAdmin)
