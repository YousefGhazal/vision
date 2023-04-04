from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models import CartVision, CartAchievements, CartNews

# Register your models here.
admin.site.unregister(Group)
admin.site.unregister(User)

admin.site.register(CartVision)
admin.site.register(CartAchievements)
admin.site.register(CartNews)
