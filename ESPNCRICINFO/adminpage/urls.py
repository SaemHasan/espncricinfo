from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.adminpage, name='adminpage'),
    path('addplayer/', include('addplayer.urls')),
    path('addground/', include('addground.urls')),
    path('addteam/', include('addteam.urls')),
]