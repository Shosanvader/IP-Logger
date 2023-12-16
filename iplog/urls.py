from django.contrib import admin
from django.urls import include, path

# Define URL patterns.
urlpatterns = [
    path('', include('ipapp.urls')),
    path('ipapp/', include('ipapp.urls')),
    path('admin/', admin.site.urls),
]
