from django.core import validators

from .models import User

from django import forms



class StudentRegistration(forms.ModelForm):

    class Meta:

        model = User

        widgets={

            'name': forms.TextInput(attrs={'class':'form-control'}),

            'email': forms.EmailInput(attrs={'class':'form-control'}),

            'password': forms.PasswordInput(render_value=True, attrs={'class':'form-control'})

        }

        fields = ['name', 'email','password']