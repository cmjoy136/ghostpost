from django import forms
from ghostpost.models import Post
from django.forms import widgets


class PostSubmit(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content', 'boast_roast']
        widgets ={
            'boast_roast': forms.RadioSelect
        } 
