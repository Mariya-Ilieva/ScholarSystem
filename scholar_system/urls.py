from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('scholar_system.users_API.urls')),
    path('user/', include('scholar_system.accounts.urls')),
    path('', include('scholar_system.main.urls')),
    path('paper/', include('scholar_system.papers.urls')),
    path('seminar/', include('scholar_system.seminars.urls')),
    path('ratings/', include('star_ratings.urls', namespace='ratings')),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler400 = 'scholar_system.main.views.bad_request'
handler403 = 'scholar_system.main.views.permission_denied'
handler404 = 'scholar_system.main.views.page_not_found'
handler500 = 'scholar_system.main.views.server_error'
