from django import forms


class AddGameForm(forms.Form):
    game_id = forms.IntegerField()
    platform = forms.ChoiceField()
