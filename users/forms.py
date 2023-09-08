from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(
        max_length=25,
        widget=forms.TextInput(attrs={"placeholder": "Max 25 Characters"}),
    )

    class Meta:
        model = User
        fields = ["username", "email", "first_name", "password1", "password2"]


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    first_name = forms.CharField(
        max_length=25,
        widget=forms.TextInput(attrs={"placeholder": "Max 25 Characters"}),
    )

    class Meta:
        model = User
        fields = ["username", "email", "first_name"]


class ProfileUpdateForm(forms.ModelForm):
    location = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Max 50 Characters"})
    )

    class Meta:
        model = Profile
        fields = ["image", "location", "bio"]

        widgets = {
            "bio": forms.Textarea(attrs={"placeholder": "Max 100 Characters"}),
        }
