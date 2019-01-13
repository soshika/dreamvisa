from django.urls import path

from . import views


urlpatterns = [
    path('', views.allvisa, name='allvisa'),
    path('<int:visa_id>/', views.detail, name='visa-detail'),
]
