from django.urls import path, include
from . import views

app_name = "blog"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("post/", views.PostListView.as_view(), name="post-list"),
    path("post/api/", views.PostListApiView.as_view(), name="post-list-api"),
    path("post/<int:pk>/", views.PostDetailView.as_view(),
         name="post-detail"),
    path("api/v1/", include("blog.api.v1.urls")),
]
