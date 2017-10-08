from django import forms
from .models import TodoList

class todoItem(forms.ModelForm):
    class Meta:
        model = TodoList
        fields = ['name', 'description',]
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'description': forms.Textarea(attrs={'class':'form-control'})
        }
