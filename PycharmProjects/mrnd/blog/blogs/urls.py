from django.conf.urls import url
from . import views
from views import *
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^$',listPosts.as_view(),name='list_posts'),
    url(r'^create/$',createPost.as_view(),name='create_post'),
    url(r'^edit/(?P<pk>[0-9]+)/$',updatePost.as_view(),name='updatePost'),
    url(r'^delete/(?P<pk>[0-9]+)/$',deletePost.as_view(),name='deletePost'),
    url(r'^(?P<pk>[0-9]+)/$',viewPost.as_view(),name='viewPost'),

]