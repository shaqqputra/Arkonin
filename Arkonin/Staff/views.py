from django.shortcuts import render
from .forms import SignUpForm
from django.urls import reverse_lazy
from django.views import generic
# Create your views here.

class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')