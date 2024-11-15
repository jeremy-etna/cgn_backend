from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from .views import (
    home,
    register,
    logged_in,
    login_view,
    need_delog,
    logout_view,
)

urlpatterns = [
    path("__reload__/", include("django_browser_reload.urls")),
    path("admin/", admin.site.urls),
    path("", home, name="home"),
    path("register/", register, name="register"),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path("need_delog/", need_delog, name='need_delog'),
    # path("", include("django.contrib.auth.urls")),
    path("logged_in", logged_in, name="logged_in"),
    path("artist/", include("users.urls.artist")),
    path("company/", include("users.urls.company")),
    path("job/", include("job.urls")),
]

# Media files serving during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
