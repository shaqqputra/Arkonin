from django import forms
from .models import Project
from django.core.files.images import get_image_dimensions
class PostForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['division','project_name', 'project_file', 'start_date', 'end_date', 'bast_date', 'bast_value']

        widgets = {
            'division' : forms.Select(attrs={'class':'form-control', 'id':'inputGroupSelect01'}),
            'project_name' : forms.TextInput(attrs={'class':'form-control round',}),
            'project_file' : forms.FileInput(attrs={'class':'form-control'}),
            'start_date' : forms.DateInput(format=('%d-%m-%Y'), attrs={'class':'form-control','type':'date','placeholder':'Select Your Date'}),
            'end_date' : forms.DateInput(format=('%d-%m-%Y'), attrs={'class':'form-control','type':'date','placeholder':'Select Your Date'}),
            'bast_date' : forms.DateInput(format=('%d-%m-%Y'), attrs={'class':'form-control','type':'date','placeholder':'Select Your Date'}),
            'bast_value' : forms.NumberInput(attrs={'class':'form-control'}),
        }
