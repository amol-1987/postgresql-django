from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from app1 import views
from django.conf.urls import url, include 
router = DefaultRouter()
#router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')
#


urlpatterns = [

    path('', include(router.urls)),
    path('gettoken/', TokenObtainPairView.as_view()),
    path('refreshtoken/', TokenRefreshView.as_view()),
]

#urlpatterns = format_suffix_patterns(urlpatterns)