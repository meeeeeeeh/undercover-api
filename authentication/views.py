import hashlib

from rest_framework import status

from rest_framework.generics import RetrieveUpdateAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView, ListAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework_simplejwt.tokens import RefreshToken, OutstandingToken, BlacklistedToken
from .serializers import UserSerializer, RegisterSerializer, ChangePasswordSerializer, \
    UpdateUserSerializer, ResetPasswordSerializer
from .models import User
from api.models import Secret


class RegisterAPIVIew(CreateAPIView):
    permission_classes = (AllowAny,)
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    swagger_schema = None

    def post(self, request, secret):
        secret1 = Secret.objects.all()[0]
        encoded_secret1 = secret1.secret.encode()
        result_secret1 = hashlib.sha256(encoded_secret1).hexdigest()

        if secret == result_secret1:
            return self.create(request)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


class UsersView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request, secret):
        secret1 = Secret.objects.all()[0]
        encoded_secret1 = secret1.secret.encode()
        result_secret1 = hashlib.sha256(encoded_secret1).hexdigest()

        if secret == result_secret1:
            return self.list(request)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


class VipUsersView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.filter(is_vip=True)
    serializer_class = UserSerializer

    def get(self, request, secret):
        secret1 = Secret.objects.all()[0]
        encoded_secret1 = secret1.secret.encode()
        result_secret1 = hashlib.sha256(encoded_secret1).hexdigest()

        if secret == result_secret1:
            return self.list(request)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


class UserRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_field = 'email'

    def get(self, request, email, secret):
        secret1 = Secret.objects.all()[0]
        encoded_secret1 = secret1.secret.encode()
        result_secret1 = hashlib.sha256(encoded_secret1).hexdigest()

        if secret == result_secret1:
            return self.retrieve(request)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, email, secret):
        secret1 = Secret.objects.all()[0]
        encoded_secret1 = secret1.secret.encode()
        result_secret1 = hashlib.sha256(encoded_secret1).hexdigest()

        if secret == result_secret1:
            return self.update(request)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, email, secret):
        secret1 = Secret.objects.all()[0]
        encoded_secret1 = secret1.secret.encode()
        result_secret1 = hashlib.sha256(encoded_secret1).hexdigest()

        if secret == result_secret1:
            return self.partial_update(request)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


class ChangePasswordView(UpdateAPIView):
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = ChangePasswordSerializer
    lookup_field = 'email'
    swagger_schema = None

    def put(self, request, email, secret):
        secret1 = Secret.objects.all()[0]
        encoded_secret1 = secret1.secret.encode()
        result_secret1 = hashlib.sha256(encoded_secret1).hexdigest()

        if secret == result_secret1:
            return self.update(request)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, email, secret):
        secret1 = Secret.objects.all()[0]
        encoded_secret1 = secret1.secret.encode()
        result_secret1 = hashlib.sha256(encoded_secret1).hexdigest()

        if secret == result_secret1:
            return self.partial_update(request)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


class UpdateProfileView(UpdateAPIView):
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = UpdateUserSerializer
    lookup_field = 'email'

    def put(self, request, email, secret):
        secret1 = Secret.objects.all()[0]
        encoded_secret1 = secret1.secret.encode()
        result_secret1 = hashlib.sha256(encoded_secret1).hexdigest()

        if secret == result_secret1:
            return self.update(request)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, email, secret):
        secret1 = Secret.objects.all()[0]
        encoded_secret1 = secret1.secret.encode()
        result_secret1 = hashlib.sha256(encoded_secret1).hexdigest()

        if secret == result_secret1:
            return self.partial_update(request)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)
    swagger_schema = None

    def post(self, request, secret):

        secret1 = Secret.objects.all()[0]
        encoded_secret1 = secret1.secret.encode()
        result_secret1 = hashlib.sha256(encoded_secret1).hexdigest()

        if secret == result_secret1:
            try:
                refresh_token = request.data['refresh_token']
                token = RefreshToken(refresh_token)
                token.blacklist()
                return Response(status=status.HTTP_205_RESET_CONTENT)
            except Exception as e:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


class LogoutAllView(APIView):
    permission_classes = (IsAuthenticated,)
    swagger_schema = None

    def post(self, request, secret):
        secret1 = Secret.objects.all()[0]
        encoded_secret1 = secret1.secret.encode()
        result_secret1 = hashlib.sha256(encoded_secret1).hexdigest()

        if secret == result_secret1:
            tokens = OutstandingToken.objects.filter(user_id=request.user.id)
            for token in tokens:
                t, _ = BlacklistedToken.objects.get_or_create(token=token)

            return Response(status=status.HTTP_205_RESET_CONTENT)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


class DeleteUserView(DestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UserSerializer
    swagger_schema = None

    def get_object(self):
        try:
            instance = self.queryset.get(email=self.request.user.email)
            return instance
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, secret):
        secret1 = Secret.objects.all()[0]
        encoded_secret1 = secret1.secret.encode()
        result_secret1 = hashlib.sha256(encoded_secret1).hexdigest()

        if secret == result_secret1:
            return self.destroy(request)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


class ResetPasswordView(UpdateAPIView):
    permission_classes = (AllowAny,)
    queryset = User.objects.all()
    serializer_class = ResetPasswordSerializer
    lookup_field = 'email'
    swagger_schema = None

    def put(self, request, email, secret):
        secret1 = Secret.objects.all()[0]
        encoded_secret1 = secret1.secret.encode()
        result_secret1 = hashlib.sha256(encoded_secret1).hexdigest()

        if secret == result_secret1:
            return self.update(request)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, email, secret):
        secret1 = Secret.objects.all()[0]
        encoded_secret1 = secret1.secret.encode()
        result_secret1 = hashlib.sha256(encoded_secret1).hexdigest()

        if secret == result_secret1:
            return self.partial_update(request)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
