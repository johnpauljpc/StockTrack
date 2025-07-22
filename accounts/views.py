from django.shortcuts import render
from django.views.generic import CreateView


from .models import CustomUser

# Create your views here.
class UserRegistrationView(CreateView):
    model = CustomUser
    fields = "__all__"
    template_name = "accounts/registration.html"