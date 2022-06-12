from django.contrib import admin

from .models import Snippet


class SnippetAdmin(admin.ModelAdmin):
    list_display = ('title', 'description',)


admin.site.register(Snippet, SnippetAdmin)
