from rest_framework.generics import ListAPIView

from main.filters import CartNewsFilter
from .models import CartVision, CartAchievements, CartNews
from .serializer import CartVisionSerializer, CartAchievementsSerializer, CartNewsSerializer
from django_filters import rest_framework as filters


class CartVisionView(ListAPIView):
    queryset = CartVision.objects.all()
    serializer_class = CartVisionSerializer

class CartAchievementsView(ListAPIView):
    queryset = CartAchievements.objects.all()
    serializer_class = CartAchievementsSerializer

class CartNewsView(ListAPIView):
    queryset = CartVision.objects.all()
    serializer_class = CartNewsSerializer


class SearchView(ListAPIView):
    # This class will search for objects based on the 'q' query parameter
    queryset = CartNews.objects.all()
    serializer_class = CartNewsSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = CartNewsFilter
    
     
    # no need to search using multiple models ..
    # i know it seems cool but it adds a high level of complixity that we don't need
    # def get_queryset(self):
    #     # This method will return the queryset based on the model name
    #     return CartNews.objects.all()


    # def get_serializer_class(self):
    #     # This method will return the serializer class based on the model name
    #     model_name = self.kwargs.get('model_name')
    #     if model_name == 'cartvision':
    #         return CartVisionSerializer
    #     elif model_name == 'cartachievements':
    #         return CartAchievementsSerializer
    #     elif model_name == 'cartnews':
    #         return CartNewsSerializer
    #     else:
    #         return None