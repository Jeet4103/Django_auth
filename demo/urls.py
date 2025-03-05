from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from core.views import home, SignupView, home_json, HomeViwew 
from rest_framework.authtoken import views
from allauth.account.views import ConfirmEmailView
from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView)
from rest_framework_simplejwt.views import TokenVerifyView


urlpatterns = [
    # Admin panel
    path('admin/', admin.site.urls),

    # Core views
    path('', home, name='home'),
    path('home/', home, name='home'),
    path('json/', HomeViwew.as_view(), name='home-json'),

    # Authentication-related URLs
    path('signup/', SignupView.as_view(), name='signup'),  # Custom signup view
    path('accounts/', include('allauth.urls')),  # Django-allauth authentication
    path('accounts/', include('django.contrib.auth.urls')),  # Default Django auth URLs

    # REST framework authenticationpath('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('api-auth/', include('rest_framework.urls')),  # DRF authentication
    path('api-token-auth/', views.obtain_auth_token),  # Token-based authentication
    path('rest-auth/', include('dj_rest_auth.urls')), # Rest-auth endpoints
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    path('account-confirm-email/<key>/', ConfirmEmailView.as_view(), name='account_confirm_email'),

    # JWT authentication
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
     path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    ]

# Serve static and media files in development mode
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
