from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer
from .models import User
from django.contrib.auth.hashers import make_password, check_password


@api_view(["POST"])
def signup(request):
    request.data["password"] = make_password(request.data["password"])
    serializer = UserSerializer(data=request.data)
    
    if serializer.is_valid(raise_exception=True):
        serializer.save()
    return Response(data=serializer.data)
    

class UserDetail(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, username):
        print("\n\n\n request:", request.headers)
        user = get_object_or_404(User, username=username)
        serializer = UserSerializer(user)
        return Response(data=serializer.data)