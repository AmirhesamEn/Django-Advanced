from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from blog.models import Post


# Create your views here.


class IndexView(TemplateView):
    """
    a class base view to show index page
    """

    template_name = "blog/test.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["name"] = "Deven"
        return context


class PostListView(ListView):
    model = Post
    context_object_name = "posts"
    template_name = "blog/list.html"
    paginate_by = 2

    def get_queryset(self):
        return super().get_queryset()


class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    context_object_name = "post"
    template_name = "blog/detail.html"

class PostListApiView(TemplateView):
    template_name = 'blog/post_list_api.html'
    