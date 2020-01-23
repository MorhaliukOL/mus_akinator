from django import forms


class FindByExcerptForm(forms.Form):
    lyrics = forms.CharField(max_length=200)