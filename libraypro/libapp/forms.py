from django.contrib.auth.forms import UserCreationForm
from libapp.models import CustomUser
from django import forms
from libapp.models import register

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model=CustomUser
        fields=UserCreationForm.Meta.fields+('email','phone')
class reisterform(forms.ModelForm):
    class Meta:
        model=register
        fields='__all__'