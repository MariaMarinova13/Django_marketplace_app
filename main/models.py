from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('name', )
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Item(models.Model):
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.CharField(max_length=1024, blank=True, null=True)
    image = models.ImageField(upload_to='item_images', blank=True, null=True)
    is_sold = models.BooleanField(default=False)
    postingDate = models.DateTimeField(auto_now_add=True)
    added_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)
    owner = models.ForeignKey(User, default=None, blank=True, on_delete=models.SET_NULL, null=True)


    def __str__(self):
        return self.name

