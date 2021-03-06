from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from PIL import Image

# ini semua model yang nantinya akan dipakai di dalam aplikasi management system ini.

# ini model divisi untuk menjelaskan detail divisi bagi setiap tenaga ahli yang ada di dalam aplikasi
class Division(models.Model):
    div_name = models.CharField(max_length=150, null = True)
    div_code = models.CharField(max_length=3, null = True)

    def __str__(self):
        return self.div_name

# ini model grade untuk menjelaskan detail jabatan bagi karyawan yang bekerja ada di dalam aplikasi
class Grade(models.Model):
    grade_name = models.CharField(max_length=150, null=True)
    grade_code = models.CharField(max_length=3, null = True)

    def __str__(self):
        return self.grade_name

# ini model karyawan secara general.
class Employee(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE, unique=True)
    nip = models.CharField(max_length=11, null = True)
    name = models.CharField(max_length=150, null = True)
    division = models.ForeignKey(Division, null = True, on_delete = models.SET_NULL)
    grade = models.ForeignKey(Grade, null = True, on_delete = models.SET_NULL)
    address = models.TextField(max_length=200, null = True)
    email = models.CharField(max_length=100, null = True)
    profile_pic = models.ImageField(default="profile1.png", null=True, blank=True, upload_to="images/profile/")

# Fungsi untuk menambahkan image ke dalam model, menggunakan package python PIL
    def save(self, *args, **kwargs):
        super(Employee, self).save(*args, **kwargs)

        img = Image.open(self.profile_pic.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.profile_pic.path)

# end comment

    def __str__(self):
        return self.name

# ini model tenaga ahli, membutuhkan model karyawan untuk membuat user Expert karena tidak semua karyawan bisa menjadi tenaga ahli (Punya role masing-masing)
class Expert(models.Model):
    exp_name = models.ForeignKey(Employee, null = True, on_delete= models.SET_NULL)
    exp_title = models.CharField(max_length=200, null = True)
    exp_education = models.CharField(max_length=200, null = True)
    exp_graduate = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return str(self.exp_name)

#  ini model SKA untuk bukti akademik bagi tenaga Ahli
class SKA(models.Model):
    exp_name = models.ForeignKey(Expert, null=True, on_delete= models.SET_NULL)
    ska_name = models.CharField(max_length=200, null = True)
    publisher = models.CharField(max_length=200, null = True)
    publish_date = models.DateField(auto_now=False, auto_now_add=False)
    expire_date = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return str(self.exp_name)

# ini model project yang akan menampung semua data-data yang ada di dalam project
class Project(models.Model):
    division = models.ForeignKey(Division, null=True, on_delete= models.SET_NULL)
    project_name = models.CharField(max_length=200, null=True)
    project_file = models.FileField()
    start_date = models.DateField(auto_now=False, auto_now_add=False)
    end_date = models.DateField(auto_now=False, auto_now_add=False)
    bast_date = models.DateField(auto_now=False, auto_now_add=False)
    bast_value = models.IntegerField(max_length=3, null = True, validators=[MinValueValidator(1), MaxValueValidator(100)])

    def __str__(self):
        return self.project_name

# ini link untuk tenaga ahli dan projek, supaya dalam satu projek bisa diisi oleh banyak tenaga ahli, dan juga supaya tenaga ahli bisa terlibat dalam semua project
class LinkProject(models.Model):
    project = models.ForeignKey(Project, null=True, on_delete= models.CASCADE)
    expert = models.ForeignKey(Expert, null=True, on_delete= models.CASCADE)

    def __str__(self):
        return str(self.project)



