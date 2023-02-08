from django.contrib.auth.models import User
from django import forms
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Повторите пароль", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ("username", "first_name", "email")

    
        

    def clean_password2(self):
        cd = self.cleaned_data
        if cd["password"] != cd["password2"]:
            raise forms.ValidationError("Пароли не совпадают!")
        return cd["password2"]
    
    
class UserCreateForm(UserCreationForm):
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Повторите пароль", widget=forms.PasswordInput)
    class Meta(UserCreationForm.Meta):
        model = User
        fields = (
            'username','first_name','email'
        )
        widgets = {
            'username': forms.TextInput(attrs={'class': "form-control"}),
            'first_name': forms.TextInput(attrs={'class': "form-control"}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password': forms.TextInput(attrs={'class': "form-control"}),
            'password2': forms.TextInput(attrs={'class': "form-control"}),
            
        }