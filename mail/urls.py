from django.urls import path, include

from mail import views

urlpatterns = [
    path('get_messages', views.get_messages)
]

