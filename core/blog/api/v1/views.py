

from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import viewsets
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from rest_framework.views import APIView
from rest_framework import status
from rest_framework import mixins

from blog.models import Category, Post

from .serializers import CategorySerializer, PostSerializer
from .paginations import DefaultPagination
from .permissions import IsOwnerOrReadOnly

# class PostList(ListCreateAPIView):
#     """
#     getting a list of posts and creating new posts
#     """
#     permission_classes = [IsAuthenticated]
#     serializer_class = PostSerializer
#     queryset = Post.objects.all()


# class PostDetail(APIView):
#     permission_classes = [IsAuthenticated,IsAuthenticatedOrReadOnly]
#     serializer_class = PostSerializer

#     def get(self, request, id):
#         post = get_object_or_404(Post, pk=id)
#         serializer = self.serializer_class(post)
#         return Response(serializer.data)
    
#     def put(self, request, id):
#         post = get_object_or_404(Post, pk=id)
#         serializer= self.serializer_class(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
    
#     def delete(self, request, id):
#         post = get_object_or_404(Post, pk=id)
#         post.delete()
#         return Response({"detail":"item removed successfully"}, status=status.HTTP_204_NO_CONTENT)

# class PostDetail(RetrieveUpdateDestroyAPIView):
#     permission_classes = [IsAuthenticated]
#     serializer_class = PostSerializer
#     queryset = Post.objects.filter(status=True)
#     lookup_field = 'id'


class PostModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['category', 'author', 'status']
    search_fields = ['title']
    ordering_fields = ['created_date']
    pagination_class = DefaultPagination

    @action(methods=['get'], detail=False)
    def get_ok(self, request):
        return Response({'detail':'ok'})

class CategoryModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    
