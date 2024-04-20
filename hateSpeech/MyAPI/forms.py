from django import forms

class detectionForm(forms.Form):
    text = forms.CharField(max_length=200)
