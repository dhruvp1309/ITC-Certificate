from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('certificates.urls')), # Replace 'certificates' with your app name if different
]