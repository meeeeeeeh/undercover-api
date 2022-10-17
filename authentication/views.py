from rest_framework import status
from rest_framework.generics import RetrieveUpdateAPIView, ListAPIView, CreateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .renders import UserJSONRenderer
from .models import User

from .serializers import RegistrationSerializer, LoginSerializer, UserSerializer


class RegistrationAPIVIew(CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer
    renderer_classes = (UserJSONRenderer,)
    #
    # def post(self, request):
    #     user = request.data.get()
    #
    #     serializer = self.serializer_class(data=user)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #
    #     return Response(serializer.data, status=status.HTTP_201_CREATED)


class LoginAPIView(APIView):
    permission_classes = (AllowAny,)
    renderer_classes = (UserJSONRenderer,)
    serializer_class = LoginSerializer

    def post(self, request):
        user = request.data.get('user', {})
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    permission_classes = (AllowAny,)
    renderer_classes = (UserJSONRenderer,)
    serializer_class = UserSerializer
    queryset = User.objects.all()

    # def update(self, request, *args, **kwargs):
    #     serializer_data = request.data.get('user', {})
    #
    #     serializer = self.serializer_class(
    #         request.user, data=serializer_data, partial=True
    #     )
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #
    #     return Response(serializer.data, status=status.HTTP_200_OK)


class UsersAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
