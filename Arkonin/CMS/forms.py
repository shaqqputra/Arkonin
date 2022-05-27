from django import forms
from .models import Project
from django.core.files.images import get_image_dimensions

class PostForm(forms.ModelForm):
    
    class Meta:
        model = Project
        fields = ['division',
        'project_name', 
        'project_file', 
        'start_date', 
        'end_date', 
        'bast_date', 
        'bast_value']
        labels = {
            'division': ('Divisi'),
            'project_name': ('Nama Projek'),
            'project_file': ('File Projek'),
            'start_date': ('Tanggal Mulai'),
            'end_date': ('Tanggal Selesai'),
            'bast_date': ('Tanggal BAST'),
            'bast_value': ('Nilai BAST')
        }

        error_messages = {
            'project_name': {
                'max_length': ("Nama Terlalu Panjang"),
            },

            'bast_value': {
                'max_length': ("Maksimal Adalah 3 Huruf!")
            },
        }

        def clean_project_name(self):
            project_name = self.cleaned_data.get('project_name')
            if not project_name:
                raise forms.ValidationError('This field is required')
            return project_name
# Validasi untuk Range Date, Tanggal Selesai Harusnya Lebih Besar Daripada Tanggal Mulai *Masih Error
        def clean(self):
            cleaned_data = super().clean()
            start_date = cleaned_data.get("start_date")
            end_date = cleaned_data.get("end_date")
            if end_date < start_date:
                raise forms.ValidationError("End date should be greater than start date.")
# End Comment

# Ini widget untuk mengatur class yang ada dalam atribut <input> di HTML (atribut <input> akan dirender dari sini)
        widgets = {
            'division' : forms.Select(attrs={'class':'form-control', 'id':'inputGroupSelect01'}),
            'project_name' : forms.TextInput(attrs={'class':'form-control round',}),
            'project_file' : forms.FileInput(attrs={'class':'form-control'}),
            'start_date' : forms.DateInput(format=('%d-%m-%Y'), attrs={'class':'form-control','type':'date','placeholder':'Select Your Date', 'id' : 'startdate'}),
            'end_date' : forms.DateInput(format=('%d-%m-%Y'), attrs={'class':'form-control','type':'date','placeholder':'Select Your Date', 'id' : 'enddate'}),
            'bast_date' : forms.DateInput(format=('%d-%m-%Y'), attrs={'class':'form-control','type':'date','placeholder':'Select Your Date'}),
            'bast_value' : forms.NumberInput(attrs={'class':'form-control',}),
        }

