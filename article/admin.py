from django.contrib import admin
from article.models import User, Article

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'country')

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'author', 'created_at', 'sign_of_publication', 'number_of_views')
    list_filter = ('author',)
    search_fields = ('title', 'content',)
