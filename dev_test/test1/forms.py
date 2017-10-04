from django import forms

class Nameform(forms.Form):
	first_name = forms.CharField(label="first name",max_length=10)
	last_name = forms.IntegerField(label="enter ur rating")

