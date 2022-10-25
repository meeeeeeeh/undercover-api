from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
from .views import UserRetrieveUpdateAPIView, RegisterAPIVIew, ChangePasswordView, UpdateProfileView, LogoutView, \
    LogoutAllView, DeleteUserView, UsersView, VipUsersView, ResetPasswordView

app_name = 'authentication'

urlpatterns = [
    path('users/<str:secret>', UsersView.as_view(), name='users'),
    path('vip_users/<str:secret>', VipUsersView.as_view(), name='vip_users'),
    path('users/<str:email>/<str:secret>', UserRetrieveUpdateAPIView.as_view()),
    path('register/<str:secret>', RegisterAPIVIew.as_view()),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('change_password/<str:email>/', ChangePasswordView.as_view(), name='auth_change_password'),
    path('update_profile/<str:email>/', UpdateProfileView.as_view(), name='auth_update_profile'),
    path('logout/', LogoutView.as_view(), name='auth_logout'),
    path('logout_all/', LogoutAllView.as_view(), name='auth_logout_all'),
    path('delete_user/', DeleteUserView.as_view(), name='delete_user'),
    path('reset_password/<str:email>', ResetPasswordView.as_view(), name='reset_password')
]
