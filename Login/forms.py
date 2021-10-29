from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserCreationForm(UserCreationForm):
    username = forms.CharField(max_length=25)
    email = forms.EmailField(required=True, label='Email')
    
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2", "password_date")

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        user.password_date = self.date.today()
        if commit:
            user.save()
        return user
