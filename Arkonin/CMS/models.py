from django.db import models
from django.contrib.auth.models import User

class Division(models.Model):
    div_name = models.CharField(max_length=150, null = True)
    div_code = models.CharField(max_length=3, null = True)

    def __str__(self):
        return self.div_name

class Grade(models.Model):
    grade_name = models.CharField(max_length=150, null=True)
    grade_code = models.CharField(max_length=3, null = True)

    def __str__(self):
        return self.grade_name


class Employee(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    nip = models.CharField(max_length=11, null = True)
    name = models.CharField(max_length=150, null = True)
    division = models.ForeignKey(Division, null = True, on_delete = models.SET_NULL)
    grade = models.ForeignKey(Grade, null = True, on_delete = models.SET_NULL)
    address = models.TextField(max_length=200, null = True)
    email = models.CharField(max_length=100, null = True)
    male = models.BooleanField(default=False)
    female = models.BooleanField(default=False)

    def __str__(self):
        return self.nip

class Expert(models.Model):
    exp_name = models.ForeignKey(Employee, null = True, on_delete= models.SET_NULL)
    exp_title = models.CharField(max_length=200, null = True)
    exp_education = models.CharField(max_length=200, null = True)
    exp_graduate = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.exp_name

class SKA(models.Model):
    exp_name = models.ForeignKey(Expert, null=True, on_delete= models.SET_NULL)
    ska_name = models.CharField(max_length=200, null = True)
    publisher = models.CharField(max_length=200, null = True)
    publish_date = models.DateField(auto_now=False, auto_now_add=False)
    expire_date = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.exp_name


class Project(models.Model):
    division = models.ForeignKey(Division, null=True, on_delete= models.SET_NULL)
    project_name = models.CharField(max_length=200, null=True)
    project_file = models.FileField()
    start_date = models.DateField(auto_now=False, auto_now_add=False)
    end_date = models.DateField(auto_now=False, auto_now_add=False)
    bast_date = models.DateField(auto_now=False, auto_now_add=False)
    bast_value = models.CharField(max_length=3, null = True)

    def __str__(self):
        return self.project_name

class LinkProject(models.Model):
    project = models.ForeignKey(Project, null=True, on_delete= models.CASCADE)
    expert = models.ForeignKey(Expert, null=True, on_delete= models.CASCADE)



