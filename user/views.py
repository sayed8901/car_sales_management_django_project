from django.shortcuts import render, redirect
from . import forms
from car.models import Car
from order.models import Order

from django.contrib import messages

# necessary importing for class view implementation
from django.contrib.auth.views import LoginView, LogoutView,PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import login, logout

# importing reverse_lazy to redirect
from django.urls import reverse_lazy

# to use login required decorator
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator



# Create your views here.
def register(request):
    if request.method == 'POST':
        register_form = forms.RegistrationForm(request.POST)

        if register_form.is_valid():
            register_form.save()
            messages.success(request, 'Account created successfully')

            return redirect('login')
    
    else:
        register_form = forms.RegistrationForm()

    return render(request, 'register.html', {'form': register_form,  'type': 'Register'})




# login using class based view
class UserLoginView(LoginView):
    template_name = 'register.html'
    # success_url = reverse_lazy('profile')

    def get_success_url(self) -> str:
        return reverse_lazy('homepage')

    def form_valid(self, form):
        messages.success(self.request, 'Logged in successfully')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.warning(self.request, 'Login information incorrect')
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'login'
        return context
    



# logout using class based view
class UserLogoutView(LogoutView):
    def get_success_url(self) -> str:
        logout(self.request)
        
        return reverse_lazy('login')



@login_required         # login required decorator
def profile(request):
    order = Order.objects.filter(user=request.user)

    return render(request, 'profile.html', {'data': order})





@login_required         # login required decorator
def edit_profile(request):
    if request.method == 'POST':
        profile_form = forms.ChangeUserForm(request.POST, instance = request.user)

        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Profile updated successfully')

            return redirect('profile')
    
    else:
        profile_form = forms.ChangeUserForm(instance = request.user)

    return render(request, 'profile_update.html', {'form': profile_form})





@login_required         # login required decorator
def password_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user = request.user, data = request.POST)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)

            messages.success(request, 'Password updated successfully')
            return redirect('profile')
    
    else:
        form = PasswordChangeForm(user = request.user)

    return render(request, 'password_change.html', {'form': form})


