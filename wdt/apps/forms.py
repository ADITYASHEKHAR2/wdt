from django import forms
from .models import user_model



class UserRegistrationForm(forms.ModelForm):

    class Meta:
        model = user_model
        fields = ('username', 'first_name', 'email','password')
        widgets = {
           'password': forms.PasswordInput(),
        }


