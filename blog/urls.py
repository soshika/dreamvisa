from django.urls import path, include

from blog import views


urlpatterns = [
    path('', views.allblog, name='allblog'),
    path('<int:blog_id>/', views.detail, name='blog-detail'),
]
