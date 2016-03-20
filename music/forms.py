from django import forms
from .models import *
from django.contrib.auth.models import User


class TopUpForm(forms.ModelForm):

    class Meta:
        model = AirtimeTopUp
        fields = ['phone_no', 'amount']

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('email', 'username', 'password')
class UserAccountForm(forms.ModelForm):
    class Meta:
        model = UserAccount
        fields = ('FirstName', 'LastName', 'phone_no',)



