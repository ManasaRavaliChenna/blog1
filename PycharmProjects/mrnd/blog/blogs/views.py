from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.http.response import Http404,HttpResponse
from django.utils.decorators import method_decorator
from django.views.generic.edit import CreateView,DeleteView,UpdateView

from blogs.models import posts
from django.core.urlresolvers import reverse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

# Create your views here.

@method_decorator(login_required, name='dispatch')
class createPost(CreateView):
    model = posts
    fields = ['title_post','info']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(createPost, self).form_valid(form)

    def get_success_url(self):
        return reverse('list_posts')


class listPosts(ListView):
    model = posts

    def get_queryset(self):
        return posts.objects.all().order_by("-timestamp")


@method_decorator(login_required, name='dispatch')
class viewPost(DetailView):
    model = posts

    def get_object(self, queryset=None):
        obj = posts.objects.get(pk=self.kwargs["pk"])
        user = self.request.user
        if obj and obj.user == user:
            return obj
        else:
            raise Http404

@method_decorator(login_required, name='dispatch')
class updatePost(UpdateView):
    model = posts
    fields = ['title_post','info']

    def get_object(self, queryset=None):
        obj = posts.objects.get(pk=self.kwargs["pk"])
        user = self.request.user
        if obj and obj.user == user:
            return obj
        else:
            raise Http404

    def form_valid(self, form):
        return super(updatePost, self).form_valid(form)

    def get_success_url(self):
        return reverse('list_posts')

@method_decorator(login_required, name='dispatch')
class deletePost(DeleteView):
    model = posts

    def get_object(self, queryset=None):
        obj = posts.objects.get(pk=self.kwargs["pk"])
        user = self.request.user
        if obj and obj.user == user:
             return obj
        else:
             raise Http404

    def get_success_url(self):
        return reverse('list_posts')
