from django import forms

class media_data(forms.Form):
    accesstoken = forms.CharField(label='Access Token', max_length=500, required=True)
    url = forms.CharField(label='URL',max_length=200, required=True)
