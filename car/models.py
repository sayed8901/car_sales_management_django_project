from django.db import models
from brand.models import Brand

# Create your models here.
class Car(models.Model):
    car_name = models.CharField(max_length=100)
    description = models.TextField()

    # image field to save image in the car app's media folder    
    # image = models.ImageField(upload_to='uploads/', blank = True, null = True)
    image = models.ImageField(upload_to='car/media/uploads/', blank = True, null = True)

    quantity = models.IntegerField()
    price = models.IntegerField()

    # One to many relationship with brand
    brand_name = models.ForeignKey(Brand, on_delete=models.CASCADE)


    def __str__(self):
        return f'{self.car_name}'


