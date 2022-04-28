from statistics import mode
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import *
from django.urls import reverse_lazy
from .forms import PostForm

class homeView(CreateView):
    model = Project
    form_class = PostForm
    template_name = 'function/add_project.html'

class addProjectView(CreateView):
    model = Project
    template_name = 'function/add_project.html'
    form_class = PostForm
    success_url = reverse_lazy('home')

