from django.urls import path, include
from mail import views, controllers

urlpatterns = [
    path('messages', controllers.get_messages),
    path('folders', controllers.get_folders),
    path('keys', controllers.get_keys),
    path('set_keys', controllers.set_keys),
    path('sign', controllers.get_sign),
    path('set_sign', controllers.set_sign),
    path('set_seen', controllers.set_seen),
]

