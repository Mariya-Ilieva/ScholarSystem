from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('scholar_system.accounts.urls')),
    path('', include('scholar_system.main.urls')),
]
