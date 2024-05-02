from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
        extra_kwargs = {'user': {'required': False}}  # user 필드를 선택적 필드로 변경

    def save(self, **kwargs):
        self.validated_data['user'] = self.context['request'].user
        return super().save(**kwargs)