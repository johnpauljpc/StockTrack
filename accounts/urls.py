from django.urls import path

from .views import (CustomRegistrationView, CustomLoginView,
                    CustomPasswordResetView, CustomPasswordResetConfirmView,
                    CustomPasswordResetDoneView, CustomPasswordResetCompleteView)


urlpatterns = [
    path('register/', view=CustomRegistrationView.as_view(), name="user_registration"),
    path("login/", view=CustomLoginView.as_view(), name="login"),

    # User's password resetting
    path('password/reset/', view=CustomPasswordResetView.as_view(), name="password_reset"),
    path('password/reset/done/', view=CustomPasswordResetDoneView.as_view(), name="password_reset_done"), #shows that reset password link has been sent.
    path("password/password/<uidb64>/<token>/", view=CustomPasswordResetConfirmView.as_view(), name="password_reset_confirm"),#generatates the reset password link
    
    path('password/reset/complete/', view = CustomPasswordResetCompleteView.as_view(), name="password_reset_complete"),
]

# - PasswordResetView sends the mail
# - PasswordResetDoneView shows a success message for the above
# - PasswordResetConfirmView checks the link the user clicked and
#   prompts for a new password
# - PasswordResetCompleteView shows a success message for the above