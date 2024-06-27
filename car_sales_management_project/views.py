from django.shortcuts import render
from car.models import Car
from brand.models import Brand

# Create your views here.
def home(request, brand_slug = None):
    car_data = Car.objects.all()        # sob post gula ke anlam
    brands = Brand.objects.all()        # sob category gulo anlam

    if brand_slug is not None:
        target_brand = Brand.objects.get(slug = brand_slug)
        car_data = Car.objects.filter(brand_name = target_brand)

    return render(request, 'home.html', {'data' : car_data, 'brand' : brands})
