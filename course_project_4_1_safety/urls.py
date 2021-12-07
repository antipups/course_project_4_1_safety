from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('mail.urls', 'mail'), namespace='mail')),
]


urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]
