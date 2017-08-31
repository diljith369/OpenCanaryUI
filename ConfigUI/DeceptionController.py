from django import forms

class ControlDeception(forms.Form):
	CHOICES = (('start','Start'),('stop','Stop'))

	controller = forms.ChoiceField(widget=forms.Select(attrs={'name': 'action'}),label="",required =False,choices=CHOICES)

