from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        extra_kwargs = {'password': {'write_only': True}}

    # def validate_password(self, value):
    #     validate_password(value)
    #     return value


class PasswordChangeSerializer(serializers.Serializer):
    before_password = serializers.CharField(required=True)
    after_password = serializers.CharField(required=True)
    confirm_password = serializers.CharField(required=True)

    def validate(self, data):
        if data.get('after_password') != data.get('confirm_password'):
            raise serializers.ValidationError("새로운 비밀번호와 확인용 비밀번호가 일치하지 않습니다.")
        return data