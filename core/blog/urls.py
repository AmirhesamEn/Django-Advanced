from django.urls import path, include
from . import views
app_name = "blog"
urlpatterns = [
    path('', views.IndexView.as_view()),
    path('list', views.PostListView.as_view()),
    path('api/v1/',include('blog.api.v1.urls') )

]