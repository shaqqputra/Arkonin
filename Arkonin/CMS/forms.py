from django import forms
from .models import Project
from django.core.files.images import get_image_dimensions
class PostForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['division','project_name', 'project_file', 'start_date', 'end_date', 'bast_date', 'bast_value']

        widget = {
            'division' : forms.Select(attrs={'class':'form-control'}),
            'project_name' : forms.TextInput(attrs={'class':'form-control'}),
            'project_file' : forms.FileInput(attrs={'class':'form-control'}),
            'start_date' : forms.DateInput(attrs={'class':'form-control'}),
            'end_date' : forms.DateInput(attrs={'class':'form-control'}),
            'bast_date' : forms.DateInput(attrs={'class':'form-control'}),
            'bast_value' : forms.NumberInput(attrs={'class':'form-control'}),
        }
