from django import forms

class PostForm(forms.Form):
    title_name = forms.CharField(max_length=255)
    description = forms.CharField(max_length=10000)
   
