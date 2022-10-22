from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
from .views import UserRetrieveUpdateAPIView, RegisterAPIVIew, ChangePasswordView, UpdateProfileView, LogoutView, \
    LogoutAllView, DeleteUserView

app_name = 'authentication'

urlpatterns = [
    path('users/<int:pk>', UserRetrieveUpdateAPIView.as_view()),
    path('register/', RegisterAPIVIew.as_view()),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('change_password/<int:pk>/', ChangePasswordView.as_view(), name='auth_change_password'),
    path('update_profile/<int:pk>/', UpdateProfileView.as_view(), name='auth_update_profile'),
    path('logout/', LogoutView.as_view(), name='auth_logout'),
    path('logout_all/', LogoutAllView.as_view(), name='auth_logout_all'),
    path('delete_user/', DeleteUserView.as_view(), name='delete_user')
]
