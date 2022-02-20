"""Main URLs module."""

from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static
from django.contrib import admin


urlpatterns = [
    # Django Admin URL
    path(settings.ADMIN_URL, admin.site.urls),
    # API URLs
    path('api/', include(('volleyball.user.urls', 'users'), namespace='users')),
    path('api/', include(('volleyball.league.urls', 'leagues'), namespace='leagues')),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
