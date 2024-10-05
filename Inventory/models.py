from django.db import models

from django.contrib.auth.models import User


class Inventory(models.Model):
    
    item = models.CharField(max_length=30)
    
    description = models.CharField(max_length=150)
    
    price = models.FloatField(default=0)
    
    quantity = models.IntegerField(default=0)
    
    review_user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    
    def __str__(self) -> str:
        
        return self.item
    
    
    
    
