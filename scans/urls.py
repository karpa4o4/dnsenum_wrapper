from django.urls import path

from . import views

app_name = 'scans'

urlpatterns = [
    path('start_scan/', views.ScanStartView.as_view()),
    path('get_status/<pk>/', views.ScanGetStatusView.as_view()),
    path('get_result/<pk>/', views.ScanGetResultView.as_view()),
]