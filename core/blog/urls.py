from django.urls import path, include
from . import views

app_name = "blog"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("list", views.PostListView.as_view(), name="post-list"),
    path("detail/<int:pk>/", views.PostDetailView.as_view(), name="post-detail"),
    path("api/v1/", include("blog.api.v1.urls")),
]
