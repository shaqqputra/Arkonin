from pyexpat import model
from django import forms
from .models import Project, Employee
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

# Employee Form untuk render form employee di bawah ini sudah ada field yang saya berikan

    class EmployeeForm(forms.ModelForm):

        class Meta:
            model = Employee
            fields = ['user',
            'nip', 
            'name', 
            'division', 
            'grade', 
            'address', 
            'email',
            'profile_pic']

            widgets = {
                'user' : forms.TextInput(attrs={'class':'form-control', 'id':'inputGroupSelect01'}),
                'nip' : forms.NumberInput(attrs={'class':'form-control round', 'placeholder':'Masukkan NIP Anda Disini',}),
                'name' : forms.TextInput(attrs={'class':'form-control round', 'placeholder':'Masukkan Nama Anda Disini',}),
                'division' : forms.Select(attrs={'class':'form-control' , 'id':'inputGroupSelect01'}),
                'grade' : forms.Select(attrs={'class':'form-control' , 'id':'inputGroupSelect01'}),
                'address' : forms.Textarea(attrs={'class':'form-control','type':'textarea','placeholder':'Masukkan Alamat Anda'}),
                'email' : forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Masukkan email anda'}),
                'profile_pic' : forms.FileInput(attrs={'class':'form-control'}),
            }

            error_messages = {
                'nip': {
                    'max_length': ("NIP Terlalu Panjang"),
                },
            }

    # Ini validasi untuk beberapa field, dan beberapa juga masih ada yang belum bisa berjalan
    # Ini Error exception MultipleChoice Return by !2 apalah itu
        def clean_user(self):
            user = self.cleaned_data.get('user')
            try:
                user = Employee.objects.get(user=user)
            except Employee.DoesNotExist:
                return user

            raise forms.ValidationError('Username Sudah Ada')

    # Yang Bawah Bisa Semua
        def clean_nip(self):
            nip = self.cleaned_data.get('nip')
            try:
                nip = Employee.objects.get(nip=nip)
            except Employee.DoesNotExist:
                return nip

            raise forms.ValidationError('NIP Sudah Dipakai')

        def clean_address(self):
            address = self.cleaned_data.get('address')
            if not address:
                raise forms.ValidationError('This field is required')
            return address

        def clean_email(self):
            email = self.cleaned_data.get('email')
            try:
                email = Employee.objects.get(email=email)
            except Employee.DoesNotExist:
                return email

            raise forms.ValidationError('This Email Address Already In Use.')
        