from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('playersingle/', views.playersingle, name='playersingle'),
    path('umpiresingle/', views.umpiresingle, name='umpiresingle'),
]