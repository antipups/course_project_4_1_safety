from django.urls import path, include
from mail import views, controllers

urlpatterns = [
    path('get_messages', controllers.get_messages),
    path('get_folders', controllers.get_folders)
]

