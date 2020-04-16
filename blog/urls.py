from django.urls import path, include
from django.conf import settings
from blog import views

app_name = 'blog'

urlpatterns = [
    path('', views.blog, name ='blog_page'),
    path('<int:blog_id>/', views.detail, name='detail'),
]
