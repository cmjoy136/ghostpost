from django import forms
from ghostpost.models import Post
from django.forms import widgets

BOOL_CHOICES = ((True, 'Boast'), (False, 'Roast'))

class PostSubmit(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content']
        widgets = forms.RadioSelect(choices=BOOL_CHOICES)
