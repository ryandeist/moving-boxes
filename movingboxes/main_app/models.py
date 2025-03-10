from django.db import models
from django.contrib.auth.models import User

BOX_SIZES = (
    ('0', 'Small'),
    ('1', 'Medium'),
    ('2', 'Large'),
    ('3', 'Extra Large')
)
# Create your models here.
class Box(models.Model):
    name = models.CharField(max_length=20)
    size = models.CharField(
        max_length=1,
        choices=BOX_SIZES,
        default=BOX_SIZES[1][0]
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    quantity = models.IntegerField()
    
    box = models.ForeignKey(Box, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    