from django.urls import path
from . import views



app_name = 'blog'

urlpatterns = [
    path('', views.home , name='home'),
    path('about/', views.about , name='blog_about'),
    path('create/', views.createBlog , name='createBlog'),
    path('<int:post_id>/show/', views.show , name='show'),
    path('<int:post_id>/delete/', views.deleteBlog , name='deleteBlog'),
    path('<int:post_id>/edit/', views.editBlog , name='editBlog'),
    path('<int:post_id>/update/', views.updateBlog , name='updateBlog'),

]
