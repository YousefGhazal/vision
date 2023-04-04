from django.db import models

# Create your models here.


class CartVision(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    logo = models.FileField(upload_to='images/', null=True, blank=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    link = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.title


class CartAchievements(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title


class CartNews(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    link = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.title
