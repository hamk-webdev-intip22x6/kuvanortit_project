from django.contrib import admin

# Register your models here.

from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'comment', 'picture', 'date')
    list_filter = ['date']
    search_fields = ['comment', 'picture']

admin.site.register(Post, PostAdmin)
