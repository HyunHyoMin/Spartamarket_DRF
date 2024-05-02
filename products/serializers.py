from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
        extra_kwargs = {'user': {'read_only': True}}

    def save(self, **kwargs):
        self.validated_data['user'] = self.context['request'].user
        return super().save(**kwargs)