from django.contrib import admin

from news.models import Tag, News


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'tag']


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'owner', 'views_count', 'date_creation']
