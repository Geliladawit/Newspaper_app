from django.contrib import admin

# Register your models here.
from .models import Article, Comment
class CommentInline(admin.TabularInline): # to make no fields appear by default
    model = Comment
class CommentInline(admin.StackedInline):
    model = Comment
    # extra = 0, optional to make no fields appear by default
class ArticleAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,
]

admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)