from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('signup/', include('signuppage.urls')),
    path('admin/', include('adminpage.urls')),
]