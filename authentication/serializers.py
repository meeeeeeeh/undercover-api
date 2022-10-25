from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.validators import UniqueValidator

from .models import User
import secrets
import string
import smtplib


# class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
#     @classmethod
#     def get_token(cls, user):
#         token = super(MyTokenObtainPairSerializer, cls).get_token(user)
#
#         token['id'] = user.id
#         token['email'] = user.email
#         return token
#

class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])

    class Meta:
        model = User
        fields = ('password', 'id', 'email', 'is_vip')

    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data['email'],
        )

        user.set_password(validated_data['password'])
        user.save()

        return user


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )

    class Meta:
        model = User
        fields = ['id',
                  'email',
                  'password',
                  'is_vip']

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)

        for key, value in validated_data.items():
            setattr(instance, key, value)

        if password is not None:
            instance.set_password(password)

        instance.save()

        return instance


class ChangePasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    old_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('old_password', 'password')

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError({"old_password": "Old password is not correct"})
        return value

    def update(self, instance, validated_data):
        user = self.context['request'].user

        if user.pk != instance.pk:
            raise serializers.ValidationError({"authorize": "You dont have permission for this user."})

        instance.set_password(validated_data['password'])
        instance.save()

        return instance


class UpdateUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)

    class Meta:
        model = User
        fields = ('email',)

    def validate_email(self, value):
        user = self.context['request'].user
        if User.objects.exclude(pk=user.pk).filter(email=value).exists():
            raise serializers.ValidationError({"email": "This email is already in use."})
        return value

    def update(self, instance, validated_data):
        user = self.context['request'].user

        if user.pk != instance.pk:
            raise serializers.ValidationError({"authorize": "You dont have permission for this user."})

        instance.email = validated_data['email']

        instance.save()

        return instance


class ResetPasswordSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)

    class Meta:
        model = User
        fields = ('email',)

    def validate_email(self, value):
        user = self.context['request'].user
        if not User.objects.exclude(pk=user.pk).filter(email=value).exists():
            raise serializers.ValidationError({"email": "This email does not exists."})
        return value

    def update(self, instance, validated_data):
        user = self.context['request'].user

        # instance.email = validated_data['email']
        #
        # instance.save()

        alphabet = string.ascii_letters + string.digits
        password = ''.join(secrets.choice(alphabet) for i in range(10))
        instance.set_password(password)
        instance.save()
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login("testmail322878@gmail.com", "thoc yuro ucji hdiz")
        server.sendmail(
            "testmail322878@gmail.com",
            instance.email,
            f"password - {password}")
        server.quit()

        return instance
