from django.urls import path
from . import views

app_name='blog'
urlpatterns=[
    path('', views.index, name='index'),
    path('posts/', views.posts, name='posts'),
    path('post/<int:post_id>/', views.post, name='post')
]