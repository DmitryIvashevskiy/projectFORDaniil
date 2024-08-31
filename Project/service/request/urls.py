from django.urls import path
from . import views

urlpatterns = [
    path('', views.request_create_view, name='request_create'),
    path('requests/', views.get_requests_view, name='get_requests'),
]