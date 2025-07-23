from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.contrib.auth import get_user_model

User = get_user_model()

@receiver(post_save, sender=User)
def send_welcome_email(sender, instance, created, **kwargs):
    if created:
        if instance.email:
            send_mail(
                subject='Welcome to STock Track Inventory System',
                message=f'Hi {instance.first_name},\n\nThanks for registering.\nWe’re glad to have you onboard!',
                from_email=None,  # uses DEFAULT_FROM_EMAIL
                recipient_list=[instance.email],
                fail_silently=False,
            )
