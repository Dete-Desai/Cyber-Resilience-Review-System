from django import forms
#from django.model import ModelForm
from django.contrib.auth import (
    authenticate,
    get_user_model

)
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
User = get_user_model()

# Create your form functions here

#AUTHENTICATION

ACCOUNT_CHOICES= [
    ('admin', 'Administrator'),
    ('cse', 'Cyber Security Expert'),
    ('ame', 'Asset Management Expert'),
    ('ccme', 'Configuration Change Management Expert'),
    ('cm', 'Controls Management Expert'),
    ('edme', 'External Dependancies Management Expert'),
    ('ime', 'Incident Management Expert'),
    ('rme', 'Risk Management Expert'),
    ('scme', 'Service Continuity Management Expert'),
    ('sae', 'Situational Awareness Expert'),
    ('tae', 'Training Awareness Expert'),
    ('vme', 'Vulnerability Management Expert')
    ]

#Registration
class CreateUserForm(UserCreationForm):
    account_type = forms.CharField(label='Account Type:', widget=forms.Select(choices=ACCOUNT_CHOICES))

    class Meta:
        model = User
        fields = ['username','email','account_type','password1','password2']

    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)
        self.fields['account_type'].empty_label = '--Choose Account--'
        
