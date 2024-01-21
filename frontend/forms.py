from django import forms

class media_data(forms.Form):
    url = forms.CharField(label='URL',max_length=200, required=True)
