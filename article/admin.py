from django.contrib import admin
from .models import Article,Comment
# Register your models here.

admin.site.register(Comment)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ["title","author","created_time"]

    list_display_links = ["title","created_time"]

    list_filter = ["created_time"]

    search_fields = ["title"]
    class Meta:
        model = Article