from django.shortcuts import render
from .forms import SignUpForm, UpdateAccount
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.models import User
# Create your views here.

class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

class UserUpdateView(generic.UpdateView):
    model = User
    form_class = UpdateAccount
    template_name = 'accounts/update_account.html'
    success_url = reverse_lazy('home')