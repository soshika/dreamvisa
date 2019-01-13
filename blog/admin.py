from django.contrib import admin
from .models import Blog


class BlogAdmin(admin.ModelAdmin):
    fields = ['title','summary', 'image', 'body', 'pub_date']
    list_display = ['title', 'image', 'summary', 'pub_date']
    search_fields = ['title', 'summary']
    list_filter = ['pub_date']

    def has_delete_permission(self, request, obj=None):
        return True


class CommentAdmin(admin.ModelAdmin):
    fields = []
    list_display = []
    raw_id_fields = []
    search_fields = []


admin.site.register(Blog, BlogAdmin)

