from rest_framework import serializers
from .models import Product, Todo
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ["task", "completed", "timestamp", "updated", "user"]


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])

    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'first_name', 'last_name')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name',
                  'email', 'is_seller', 'date_joined']
        extra_kwargs = {
            'password': {'write_only': True}
        }


# class UserLogoutSerializer(serializers.ModelSerializer):
#     token = serializers.CharField()
#     status = serializers.CharField(required=False, read_only=True)

#     def validate(self, data):
#         token = data.get("token", None)
#         print(token)
#         user = None
#         user = User.objects.get(auth_token=token)
#         user.ifLogged = False
#         user.token = ""
#         user.save()
#         data['status'] = "User is logged out."
#         return data

#     class Meta:
#         model = User
#         fields = (
#             'token',
#             'status',
#         )

class UserLoginSerializer(serializers.ModelSerializer):

    username = serializers.CharField(
        required=False,
        allow_blank=True,
        write_only=True,
    )

    email = serializers.EmailField(
        required=False,
        allow_blank=True,
        write_only=True,
        label="Email Address"
    )

    token = serializers.CharField(
        allow_blank=True,
        read_only=True
    )

    password = serializers.CharField(
        required=True,
        write_only=True,
        style={'input_type': 'password'}
    )

    class Meta(object):
        model = User
        fields = ['email', 'username', 'password', 'token']

    def validate(self, data):
        email = data.get('email', None)
        username = data.get('username', None)
        password = data.get('password', None)

        if not email and not username:
            raise serializers.ValidationError(
                "Please enter username or email to login.")

        #user = User.objects.get(username=username)
        user = authenticate(username=username, password=password)
        token, created = Token.objects.get_or_create(user=user)
        data['token'] = token
        return data
