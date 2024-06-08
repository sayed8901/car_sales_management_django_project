from django.shortcuts import render
from . import models
from . import forms

# necessary importing for class view implementation
from django.views.generic import CreateView
from django.urls import reverse_lazy



# Create your views here.
class AddBrandView(CreateView):
    model = models.Brand
    form_class = forms.BrandForm
    template_name = 'add_brand.html'
    success_url = reverse_lazy('homepage')


