from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms import fields
from django.forms.widgets import MultiWidget, RadioSelect, Select
from .models import FantasyTeam, Proxy

class PlaceBet(forms.Form):
    bet = forms.CharField(label="Bet", max_length=3)

class CreateUserForm(UserCreationForm):
    sleeperId = forms.CharField(max_length=18, required=True, label='Sleeper Id')
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'sleeperId']

    def clean_sleeperId(self):
        id = self.cleaned_data.get('sleeperId')
        
        if not self._idExists(id):
            print('should have raised')
            raise forms.ValidationError('Your Sleeper ID does not exist.')
        return id

    def _idExists(self, id):
        fantasyTeams = FantasyTeam.objects.all()
        for team in fantasyTeams:
            if id == team.sleeperId:
                return True
            else:
                pass

        return False

class AuthenticationFormWithInActiveUsers(AuthenticationForm):
    def confirm_login_allowed(self, user):
        return super().confirm_login_allowed(user)

class SelectBetsForm(forms.Form):
    teamsList = (
        ('Team1', 'Team 11'),
        ('Team2', 'Team 22'),
        ('Team3', 'Team 33'),
    )
    fields = forms.MultipleChoiceField(choices=teamsList)


    