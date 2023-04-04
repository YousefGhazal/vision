from rest_framework.serializers import ModelSerializer
from .models import CartVision, CartAchievements, CartNews


class CartVisionSerializer(ModelSerializer):
    class Meta:
        fields = "__all__"
        model = CartVision


class CartAchievementsSerializer(ModelSerializer):
    class Meta:
        fields = "__all__"
        model = CartAchievements


class CartNewsSerializer(ModelSerializer):
    class Meta:
        fields = "__all__"
        model = CartNews
