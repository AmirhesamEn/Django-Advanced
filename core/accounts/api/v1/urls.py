from django.urls import path
# from rest_framework.authtoken.views import ObtainAuthToken
from . import views

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

app_name = "api-v1"
urlpatterns = [
    # registration
    path('registration/', views.RegistrationApiView.as_view(), name='registration'),

    path('test-email/', views.EmailTestSend.as_view(), name='test-email'),
    # activation
    path('activation/confirm/<str:token>', views.ActivationApiView.as_view(), name="activation"),

    # resent activation
    path('activation/resend', views.ActivationResendApiView.as_view(), name="activation-resend"),

    # change password
    path('change-password/', views.ChangePasswordApiView.as_view(), name="change-password"),

    # reset password

    # login token
    path('token/login/', views.CustomObtainAuthToken.as_view(), name='token-login'),
    path('token/logout/', views.CustomDiscardAuthToken.as_view(), name='token-login'),

    # login jwt
    path('jwt/create/', views.CustomTokenObtainPairView.as_view(), name='jwt-create'),
    path('jwt//refresh/', TokenRefreshView.as_view(), name='jwt_refresh'),
    path('jwt/verify/', TokenVerifyView.as_view(), name='jwt_refresh'),

    # profile\
    path('profile', views.ProfileApiView.as_view(), name='profile'),
]