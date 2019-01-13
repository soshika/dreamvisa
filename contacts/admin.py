from django.contrib import admin

# Register your models here.

from django.contrib import admin

from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    fields = ['name', 'phone', 'email', 'subject', 'message']
    list_display = ['name', 'phone', 'email', 'subject', 'message']
    search_fields = ['name', 'phone', 'email', 'subject', 'message']

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return True


admin.site.register(Contact, ContactAdmin)

