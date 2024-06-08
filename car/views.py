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




# detailsView class
class DetailCarView(DetailView):
    model = models.Car
    pk_url_kwarg = 'id'
    template_name = 'car_details.html'

    def post(self, request, *args, **kwargs):
        comment_form = forms.CommentForm(data = self.request.POST)
        car = self.get_object() # current car er ekta object

        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.car = car
            new_comment.save()
        
        return self.get(request, *args, **kwargs)


    # to get comments data as context
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        car = self.get_object()

        comments = car.comments.all()
        comment_form = forms.CommentForm()
        
        context['comments'] = comments
        context['comment_form'] = comment_form

        return context


