from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetConfirmView, PasswordResetDoneView, PasswordResetCompleteView

from .forms import CustomUserCreationForm


from .models import CustomUser

# Create your views here.
class CustomRegistrationView(CreateView):
    model = CustomUser
    form_class = CustomUserCreationForm
    template_name = "accounts/registration.html"

class CustomLoginView(LoginView):
    template_name = "accounts/login.html"
    
class CustomPasswordResetView(PasswordResetView):
    email_template_name = "accounts/password_reset_email.html"
    template_name = "accounts/password_reset_form.html"
    


class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = "accounts/password_reset_done.html"

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = "accounts/password_reset_confirm.html"
    success_url = reverse_lazy('password_reset_complete')



class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = "accounts/password_reset_complete.html"
