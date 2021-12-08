from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import FantasyTeam, Proxy

class PlaceBet(forms.Form):
    bet = forms.CharField(label="Bet", max_length=3)

class CreateUserForm(UserCreationForm):
    sleeperId = forms.IntegerField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'sleeperId']

class AuthenticationFormWithInActiveUsers(AuthenticationForm):
    def confirm_login_allowed(self, user):
        return super().confirm_login_allowed(user)



    