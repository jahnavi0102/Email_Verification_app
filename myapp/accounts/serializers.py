from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, get_user_model
from djoser.conf import settings
from djoser.serializers import TokenCreateSerializer

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

        return user



User = get_user_model()

# class CustomTokenCreateSerializer(TokenCreateSerializer):

#     def validate(self, attrs):
#         password = attrs.get("password")
#         params = {settings.LOGIN_FIELD: attrs.get(settings.LOGIN_FIELD)}
#         self.user = authenticate(
#             request=self.context.get("request"), **params, password=password
#         )
#         if not self.user:
#             self.user = User.objects.filter(**params).first()
#             if self.user and not self.user.check_password(password):
#                 self.fail("invalid_credentials")
#         # We changed only below line
#         if self.user: # and self.user.is_active: 
#             return attrs
#         self.fail("invalid_credentials")        