from django import forms
from rbac import models


class LoginForm(forms.ModelForm):
    class Meta:
        model = models.UserInfo
        fields = ['name', 'password']
        widgets = {
            'password': forms.TextInput(attrs={'type': 'password'})
        }
