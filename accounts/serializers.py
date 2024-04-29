from django.contrib.auth.password_validation import validate_password, password_changed
from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
    
    # def validate_password(self, value):
    #     validate_password(value)
    #     return value