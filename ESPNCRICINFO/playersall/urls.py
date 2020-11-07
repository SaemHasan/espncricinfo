from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('playersall/', views.playersall, name='playersall'),
    path('umpiresall/', views.umpires, name='umpiresall'),
    path('', include('playersingle.urls')),
]