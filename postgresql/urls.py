from django.conf.urls import url, include 
from django.urls import path
from django.contrib import admin

urlpatterns = [ 
    path('admin/', admin.site.urls),
    url(r'^', include('app1.urls')),
]
