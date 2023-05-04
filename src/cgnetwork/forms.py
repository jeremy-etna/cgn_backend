from django.contrib.auth.forms import UserCreationForm
from users.models.common import CustomUser


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['role',
                  'email',
                  ]
