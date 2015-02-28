
from django import forms

class DestinyQuestFightForm(forms.Form):
	player_brawn = forms.IntegerField(initial = 0)
	player_speed = forms.IntegerField(initial = 0)
	player_armour = forms.IntegerField(initial = 0)
	player_health = forms.IntegerField(initial = 0)
	
	monster_name = forms.CharField()
	monster_brawn = forms.IntegerField(initial = 0)
	monster_speed = forms.IntegerField(initial = 0)
	monster_armour = forms.IntegerField(initial = 0)
	monster_health = forms.IntegerField(initial = 0)
	