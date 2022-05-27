from statistics import mode
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import *
from django.urls import reverse_lazy
from .forms import PostForm

class HomeView(CreateView):
    model = Project
    form_class = PostForm
    template_name = 'index.html'

# Class View untuk Model Project dari detail hingga delete
class ProjectView(ListView):
    model = Project
    template_name = 'data/table_project.html'
    ordering = ['-start_date']

class AddProjectView(CreateView):
    model = Project
    template_name = 'function/add_project.html'
    form_class = PostForm
    success_url = reverse_lazy('home')

class UpdateProjectView(UpdateView):
    model = Project

# end comment

# Class View untuk Model Karyawan dari detail hingga delete
class AddEmployeeView(CreateView):
    model = Employee

# end Comment