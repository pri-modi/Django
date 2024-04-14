from django.urls import path
from . import views

urlpatterns = [
    path("speechcontrol/", views.speechDetectionListCreate.as_view(), name="speechdetection-view-create")
]