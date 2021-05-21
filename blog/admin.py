from operator import pos
from django.contrib import admin
from .models import Post, Comment

class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'title')
    fieldsets = [
        (None, { 'fields': [('title','text', 'created_date', 'published_date', 'images')] } ),
    ]

    def save_model(self, request, obj, form, chang):
        if getattr(obj, 'author', None) is None:
            obj.author = request.user
        obj.save()

admin.site.register(Comment)
admin.site.register(Post, PostAdmin)
