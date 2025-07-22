from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()
class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['email',"first_name", "last_name", 'password1', 'password2']