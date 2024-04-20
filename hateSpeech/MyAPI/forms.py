from django import forms

class detectionForm(forms.Form):
    # text = forms.CharField(max_length=1000, widget=forms.TextInput(attrs={'placeholder':'Enter text'}))
    text = forms.CharField(
        max_length=1000,
        widget=forms.Textarea(attrs={'placeholder': 'Enter text', 'rows': 5, 'style': 'width: 100%;'}),  # Changed to Textarea
    )