from django.urls import path
from . import views

# Define URL patterns for the app.
urlpatterns = [
    path('', views.home, name='home'),
    path('current-ip/', views.current_ip, name='current_ip'),
    path('view-ips/', views.view_logged_ips, name='view_logged_ips'),
]