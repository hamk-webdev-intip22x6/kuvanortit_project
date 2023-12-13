from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *
from . import views

app_name = "gallery"
urlpatterns = [
    path("", views.GalleryView.as_view(), name="index"),
    path("user/<user>/", views.UserListView.as_view(), name="user"),
    path("folder/<int:pk>/", views.FolderListView.as_view(), name="folder"),
    path(
        "folder/<int:pk>/delete", views.FolderDeleteView.as_view(), name="delete_folder"
    ),
    path("image_upload", image_upload, name="image_upload"),
    path("create_folder", create_folder, name="create_folder"),
    path("success", success, name="success"),
    path("search/", SearchResultsView.as_view(), name="search_results"),
    path("<int:pk>/delete", PictureDeleteView.as_view(), name="delete_picture"),
    path("<int:pk>/edit", PictureEditView.as_view(), name="edit_picture"),
]
