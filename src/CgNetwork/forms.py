from django.contrib.auth.forms import UserCreationForm
from CgNetwork.models import CustomUser


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['user_role', 'email']
