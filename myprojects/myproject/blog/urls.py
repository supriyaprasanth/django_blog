from django.conf.urls import url
from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    url(r'^post/(?P<pk>\d+)/remove/$', views.post_remove, name='post_remove'),
    url(r'^post/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
    #url(r'^comment/(?P<pk>\d+)/approve/$', views.comment_approve, name='comment_approve'),
	#url(r'^comment/(?P<pk>\d+)/remove/$', views.comment_remove, name='comment_remove'),

]