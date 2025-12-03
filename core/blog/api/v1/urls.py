from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter, SimpleRouter
app_name = "api-v1"

# router = DefaultRouter()
router = SimpleRouter()
router.register('post', views.PostModelViewSet, basename='post')
router.register('category', views.CategoryModelViewSet, 'category')
urlpatterns = router.urls

# urlpatterns = [
#     # path('posts/', views.PostList.as_view(), name='post-list'),  
#     # path('post/<int:id>', views.PostDetail.as_view(), name='post-detail'),

#     path('post/', views.PostViewSet.as_view({'get':'list', 'post':'create'}), name='post-list'),
#     path('post/<int:pk>', views.PostViewSet.as_view({'get':'retrieve', 'put':'update', 'patch':'partial_update', 'delete':'destroy'}), name='post-list'),

# ]