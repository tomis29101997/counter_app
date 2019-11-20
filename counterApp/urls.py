from django.urls import path
from . import views
from django.http import HttpResponse


urlpatterns = [
 path('', views.home, name='home'),
 path('about/', views.about_view, name='about'),
 path('count/', views.count, name='countJmeno'),
]
