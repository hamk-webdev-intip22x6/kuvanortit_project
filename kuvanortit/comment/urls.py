from django.urls import path
from . import views

app_name = "comment"
urlpatterns = [
    path("<int:pk>/", views.CommentListView.as_view(), name="index"),
    path("<int:post_id>/add", views.PostView.as_view(), name="post"),
    path(
        "<int:post_id>/comment/<int:pk>/delete",
        views.CommentDeleteView.as_view(),
        name="delete",
    ),
]
