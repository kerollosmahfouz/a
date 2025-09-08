from django import forms
from .models import cont

class contform(forms.ModelForm):
    class Meta :
        model = cont
        fields = ['name','pnum']