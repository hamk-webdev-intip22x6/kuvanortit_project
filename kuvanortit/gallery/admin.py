from django.contrib import admin
from .models import Picture, PictureFolder


class FolderAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "pub_date", "mod_date", "user")
    search_fields = ["title", "description", "tags"]
    list_filter = ["pub_date", "mod_date"]


class PictureAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "description",
        "tags",
        "image",
        "pub_date",
        "mod_date",
        "folder",
        "private",
    )
    search_fields = ["title", "description", "tags"]
    list_filter = ["pub_date", "mod_date"]


admin.site.register(Picture, PictureAdmin)
admin.site.register(PictureFolder, FolderAdmin)
