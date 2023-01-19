from django import forms
from .models import list_todo


class ListForm(forms.ModelForm):
    class Meta:
        model = list_todo
        fields = ['title', 'aciklama', 'date', 'finished']
