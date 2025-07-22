from django import template
from django.contrib.auth import get_user_model

register = template.Library()
User = get_user_model()

@register.filter(name='user_from_email')
def user_from_email(email):
    try:
        user = User.objects.get(email=email)
        print("user: ", user)
        return user.first_name
    except User.DoesNotExist:
        print("nothing here")
        return None
