from django.shortcuts import (render,
							  HttpResponseRedirect,
							  reverse)
from django.http import JsonResponse
from django.views.generic import (TemplateView,
								  CreateView,
								  ListView,
								  DetailView,
								  UpdateView,
								  DeleteView)
from .forms import PostForm
from .models import Post
from django.urls import reverse_lazy


# make home and postlist as one
class Home(ListView):
    '''View list of all Post.'''
    model = Post
    template_name = 'blog/index.html'

    def get_queryset(self):
        return Post.objects.all().order_by('-updated')


class NewPost(CreateView):
    '''Create new Post.'''
    form_class = PostForm
    template_name = 'blog/newpost.html'


class PostDetail(DetailView):
    '''View Post.'''
    model = Post
    slug_field = 'slug'
    template_name = 'blog/postdetail.html'


class PostUpdate(UpdateView):
    '''Update the Post.'''
    model = Post
    form_class = PostForm
    slug_field = 'slug'
    template_name = 'blog/newpost.html'


def post_delete(request, method=['POST']):
    '''Delete the Post'''
    print("got accessed")
    id = request.POST.get('id')
    print(id)
    try:
        Post.objects.get(id=id).delete()
        result = {"deleted": True}
    except:
        result = {"deleted": False}
    print(result)
    return JsonResponse(result)

