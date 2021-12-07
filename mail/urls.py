from django.contrib import admin
from django.urls import path, include

from mail import views

urlpatterns = [
    path('', views.MailListView.as_view(), name='mails_list'),
    path('create_mail', views.CreateMail.as_view(), name='create_mail')
]

