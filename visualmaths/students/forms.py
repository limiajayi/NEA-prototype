from django import forms
from .models import StudentUser, Question



class SignupForm(forms.ModelForm):
    password = forms.CharField(max_length=250, widget = forms.PasswordInput())

    class Meta:
        model = StudentUser
        fields = ["username", "password", "maths", "further_maths",]
        labels = {
            "username": "Username",
            "password": "Password",
            "maths": "Maths",
            "further_maths": "Further Maths",
        }

class LoginForm(forms.ModelForm):
    password = forms.CharField(max_length=250, widget = forms.PasswordInput())
    
    class Meta:
        model = StudentUser
        fields = ["username", "password",]
        labels = {
            "username": "Username",
            "password": "Password",
        }

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ["subject", "topic", "difficulty"]
