from django.shortcuts import render, redirect
from . import models
from . import forms

# necessary importing for class view implementation
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy

# to use login required decorator
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator



# Create your views here.
@login_required
def add_car(request):
    if request.method == 'POST':
        form = forms.CarForm(request.POST)

        if form.is_valid():
            form.save()
            print(form.cleaned_data)
            return redirect('homepage')
    else:
        form = forms.CarForm()

    return render(request, 'add_car.html', {'form': form})




@method_decorator(login_required, name='dispatch')
class AddCarView(CreateView):
    model = models.Car
    form_class = forms.CarForm
    template_name = 'add_car.html'
    success_url = reverse_lazy('homepage')

