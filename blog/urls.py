from django.urls import path
from django.conf.urls import include
from blog import views


app_name = 'blog'

urlpatterns = [
    path('', views.blog_home),
    path('<category>', views.blog_category, name='blog_category'),
    path('<category>/<post_id>', views.blog_post, name='blog_post'),
]
