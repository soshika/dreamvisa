from django.urls import path

from . import views


urlpatterns = [
    path('', views.allcountries, name='allcountries'),
    path('<int:country_id>/', views.detail, name='country-detail'),
]
