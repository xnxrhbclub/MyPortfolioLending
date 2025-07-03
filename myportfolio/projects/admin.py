from django.contrib import admin
from .models import GitHubProject


@admin.register(GitHubProject)
class GitHubProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'language', 'stars', 'updated_at')
    search_fields = ('name', 'language')
    list_filter = ('language',)