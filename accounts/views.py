from django.shortcuts import get_object_or_404
from django.contrib.auth.hashers import make_password, check_password
from django.http import JsonResponse
from django.contrib.auth import logout as auth_logout
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes, authentication_classes
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenBlacklistView
from .serializers import UserSerializer, PasswordChangeSerializer, UserUpdateSerializer
from .models import User


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


class UserManagement(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            tokens = get_tokens_for_user(serializer.instance)
            return Response(data=tokens, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request):
        user = User.objects.get(id=request.user.id)
        if check_password(request.data["password"], user.password):
            user.delete()
            return Response(data={"message":"회원탈퇴 성공"}, status=status.HTTP_200_OK)
        else:
            return Response(data={"message":"비밀번호 불일치"}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        user = User.objects.get(id=request.user.id)
        serializer = PasswordChangeSerializer(data=request.data, context={'request':request})
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response({"message": "비밀번호가 성공적으로 변경되었습니다."}, status=status.HTTP_200_OK)


class UserDetail(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get(self, request, username):
        user = get_object_or_404(User, username=username)
        serializer = UserSerializer(user)
        return Response(data=serializer.data)

    def put(self, request, username):
        user = get_object_or_404(User, username=username)
        serializer = UserUpdateSerializer(data=request.data, instance=user, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(data=serializer.data)

