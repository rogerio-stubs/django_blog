from django.contrib import admin

from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # list_display = ('title', 'slug', 'author', 'created', 'updated')
    list_display = ("title", "slug", "author", "created")
    prepopulated_fields = {'slug': ('title',)}
