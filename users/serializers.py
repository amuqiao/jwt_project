from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth import authenticate

# 自定义用户序列化器
class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'email')

# 用户注册序列化器
class UserSignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('email', 'password')

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user

# 登录序列化器
class UserSignInSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(username=data['email'], password=data['password'])
        if not user:
            raise serializers.ValidationError('Invalid credentials')
        return user
