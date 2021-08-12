from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('blog/<int:pk>',views.blog_detail,name="blog"),
    path('add/',views.add_blog,name="add_blog"),
]