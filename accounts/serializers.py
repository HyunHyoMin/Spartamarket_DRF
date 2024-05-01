from django.core import exceptions
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.hashers import check_password, make_password
from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, data):
        user = User(**data)
        password = data.get('password')

        if password:
            errors = dict()
            try:
                validate_password(password=password, user=user)
            except exceptions.ValidationError as e:
                errors['password'] = list(e.messages)

            if errors:
                raise serializers.ValidationError(errors)

        return super().validate(data)

    def save(self, **kwargs):
        password = make_password(self.validated_data['password'])
        self.validated_data['password'] = password
        return super().save(**kwargs)


class PasswordChangeSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
    confirm_password = serializers.CharField(required=True)


    def validate(self, data):
        user = self.context['request'].user
        password = data.get('new_password')
        
        if password:
            errors = dict()
            try:
                validate_password(password=password, user=user)
            except exceptions.ValidationError as e:
                errors['password'] = list(e.messages)
            
            if errors:
                raise serializers.ValidationError(errors)

        if data.get('new_password') != data.get('confirm_password'):
            raise serializers.ValidationError("새 비밀번호가 서로 일치하지 않습니다.")
        
            
        if not user.check_password(data.get("old_password")):
            raise serializers.ValidationError("현재 비밀번호가 일치하지 않습니다.")

        if user.check_password(data.get("new_password")):
            raise serializers.ValidationError("새 비밀번호가 현재 비밀번호와 같습니다.")
            
        return data

    def save(self, **kwargs):
        user = self.context['request'].user
        user.set_password(self.validated_data['new_password'])
        user.save()
        return user


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['password']