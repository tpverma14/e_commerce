from django.contrib import admin

from .models import Blog, Comment



class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'updated', 'timestamp')
    prepopulated_fields = {"slug": ("title",)}


class CommentAdmin(admin.ModelAdmin):
    readonly_fields = ("comment", "email")



admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment, CommentAdmin)


