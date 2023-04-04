from django.urls import path
from .views import CartVisionView, CartAchievementsView, CartNewsView, SearchView

urlpatterns = [
    path("vision/", CartVisionView.as_view()),
    path("achievements/", CartAchievementsView.as_view()),
    path("news/", CartNewsView.as_view()),
    path('search/', SearchView.as_view()),
]
