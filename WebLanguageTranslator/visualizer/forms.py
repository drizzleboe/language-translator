from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


#Creating a form here
class signup_form(forms.ModelForm):
    class Meta:
        model = User
        fields=['email']

class signin_form(forms.ModelForm):
    class Meta:
        model = User
        fields=['email','password']

class TextInputForm(forms.Form):
    text_input = forms.CharField(label='', max_length=100, 
                                 initial='',
                                 widget=forms.Textarea(attrs={'rows': 4, 'cols': 40})
                                 )

