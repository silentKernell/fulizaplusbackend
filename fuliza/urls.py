from django.urls import path
from .views import DataCaptureView

urlpatterns = [
    path('v1/uplink/', DataCaptureView.as_view(), name='data_capture'),
]