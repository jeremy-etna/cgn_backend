from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import home, register, logged_in
from django.contrib import admin

urlpatterns = [
    path("__reload__/", include("django_browser_reload.urls")),
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('register/', register, name='register'),
    path('', include('django.contrib.auth.urls')),  # Auth views (login, logout, password reset, etc.)
    path('logged_in', logged_in, name='logged_in'),  # Logged in view
    path('artist/', include('users.urls.artist')),
    path('company/', include('users.urls.company')),
    path('job/', include('job.urls')),
]

# Media files serving during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
