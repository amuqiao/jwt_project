from rest_framework import status, permissions, generics
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from .models import CustomUser
from .serializers import UserSignUpSerializer, UserSignInSerializer, CustomUserSerializer

# 用户注册视图
class UserSignUpView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSignUpSerializer

# 用户登录视图
class UserSignInView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserSignInSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            refresh_token = str(refresh)
            return Response({
                'access_token': access_token,
                'refresh_token': refresh_token
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 获取用户信息视图
class UserMeView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = request.user
        serializer = CustomUserSerializer(user)
        return Response(serializer.data)
