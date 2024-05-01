from django import forms

class PostForm(forms.Form):
    title_name = forms.CharField(max_length=255)
    description = forms.CharField(max_length=10000)
    date_created = forms.DateTimeField(auto_now_add=True)
    date_updated = forms.DateTimeField(auto_now=True)