from django import forms

class detectionForm(forms.Form):
    text = forms.CharField(max_length=1000, widget=forms.TextInput(attrs={'placeholder':'Enter text'}))
