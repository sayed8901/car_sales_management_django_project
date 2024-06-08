from django.db import models

# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200)

    def __str__(self):
        return f'{self.name}'
