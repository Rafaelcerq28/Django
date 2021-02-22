from django import forms
from django.forms import widgets
from .models import Task

class TaskForm(forms.ModelForm):
    
    class Meta:
        model = Task
        fields = ('title','description')

        #Inserindo CSS no formulario
        #widgets = {
            #'title': forms.TextInput(attrs={'class': 'form-control'}),
            #'description': forms.Textarea(attrs={'class': 'form-control'})
        #}
