from django.contrib import admin
from django.urls import path, include
urlpatterns=[path('admin/', admin.site.urls), path('api/farms/', include('apps.farms.urls')), path('api/crops/', include('apps.crops.urls'))]
