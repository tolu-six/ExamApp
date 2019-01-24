from django import forms

from .models import Assignment

class AssignmentForm(forms.ModelForm): #Django Form
    class Meta:
        model = Assignment #This is the model class
        #The DB felds
        #fields = '__all__'
        fields = [ 'name', 'instruction', 'start_date', 'end_date', 'category', 'show_result', 'show_instruction', 'is_active']
        input_formats = ['%d/%m/%Y %H:%M']
        widgets = {
        'start_date': forms.DateTimeInput(attrs={'type':'text', 'data-toggle': 'datetimepicker',  'data-target': '#id_start_date' ,'class': 'form-control datetimepicker-input'}),
        'end_date': forms.DateTimeInput(attrs={'type':'text','class': 'form-control datetimepicker-input', 'data-toggle':"datetimepicker", 'data-target':"#id_end_date"}),
        }

# venv


