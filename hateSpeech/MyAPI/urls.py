from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('MyAPI', views.detectionView)
urlpatterns = [
    path('api/', include(router.urls)),
    path('status/', views.detecting),
    path('form/', views.xyz, name='xyzform'),
]