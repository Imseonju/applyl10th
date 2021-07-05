from django.contrib.auth.forms import UserCreationForm
from django.forms import fields
from .models import CustomUser

class RegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password1', 'password2', 'realname', 's_num', 's_dept']