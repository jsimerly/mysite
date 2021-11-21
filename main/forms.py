from django import forms

class PlaceBet(forms.Form):
    bet = forms.CharField(label="Bet", max_length=3)
    