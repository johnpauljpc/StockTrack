from django.urls import path

from .views import UserRegistrationView


urlpatterns = [
    path('register/', view=UserRegistrationView.as_view(), name="user_registration"),
]