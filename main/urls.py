from django.urls import path
from .views import CartVisionView, CartAchievementsView, CartNewsView

urlpatterns = [
    path("vision/", CartVisionView.as_view()),
    path("achievements/", CartAchievementsView.as_view()),
    path("news/", CartNewsView.as_view()),
]
