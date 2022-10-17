from django.urls import path

from .views import RegistrationAPIVIew, LoginAPIView, UserRetrieveUpdateAPIView, UsersAPIView

app_name = 'authentication'

urlpatterns = [
    path('users/', UsersAPIView.as_view()),
    path('users/<int:pk>', UserRetrieveUpdateAPIView.as_view()),
    path('users/registration/', RegistrationAPIVIew.as_view()),
    path('users/login/', LoginAPIView.as_view()),
]
