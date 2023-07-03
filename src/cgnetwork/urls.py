from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


from .views import (
    home,
    activate,
    logged_in,
    need_delog,
    # R E S T
    RegisterView,
    LoginView,
    LogoutView,
    GetUserView,
)


urlpatterns = [
    path("__reload__/", include("django_browser_reload.urls")),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path("admin/", admin.site.urls),

    path("register/", RegisterView.as_view(), name="register"),
    path('activate/<uidb64>/<token>/', activate, name='activate'),

    path('login/', LoginView.as_view(), name='login'),
    path("get_user/", GetUserView.as_view(), name="test_auth"),
    path("logout/", LogoutView.as_view(), name="logout"),

    path("need_delog/", need_delog, name='need_delog'),
    path("logged_in", logged_in, name="logged_in"),
    path("artist/", include("users.urls.artist")),
    path("company/", include("users.urls.company")),
    path("job/", include("job.urls")),
    path("post/", include("post.urls")),
]

# Media files serving during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
