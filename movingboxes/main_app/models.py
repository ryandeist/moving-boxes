from django.db import models

BOX_SIZES = (
    ('S', 'Small'),
    ('M', 'Medium'),
    ('L', 'Large'),
    ('XL', 'Extra Large')
)
# Create your models here.
class Box(models.Model):
    name = models.CharField(max_length=20)
    size = models.CharField(
        max_length=2,
        choices=BOX_SIZES,
        default=BOX_SIZES[1][0]
    )
    
    def __str__(self):
        return self.name