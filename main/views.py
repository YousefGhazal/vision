from rest_framework.generics import ListAPIView
from .models import CartVision, CartAchievements, CartNews
from .serializer import CartVisionSerializer, CartAchievementsSerializer, CartNewsSerializer


class CartVisionView(ListAPIView):
    queryset = CartVision.objects.all()
    serializer_class = CartVisionSerializer

class CartAchievementsView(ListAPIView):
    queryset = CartAchievements.objects.all()
    serializer_class = CartAchievementsSerializer

class CartNewsView(ListAPIView):
    queryset = CartVision.objects.all()
    serializer_class = CartNewsSerializer
