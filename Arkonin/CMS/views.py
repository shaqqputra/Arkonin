from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import *
from django.urls import reverse_lazy
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from .forms import PostForm, EmployeeForm


    
class HomeView(ListView):
    model = Project
    form_class = PostForm
    template_name = 'index.html'
    def get_context_data(self, *args, **kwargs):
        list_emp = Employee.objects.all()
        list_proj = Project.objects.all()
        list_exp = Expert.objects.all()
        employee_count = Employee.objects.all().count()
        division_count = Division.objects.all().count()
        project_count = Project.objects.all().count()
        expert_count = Expert.objects.all().count()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context ["list_emp"] = list_emp
        context ["list_proj"] = list_proj
        context ["list_exp"] = list_exp
        context ["employee_count"] = employee_count
        context ["project_count"] = project_count
        context ["expert_count"] = expert_count
        context ["division_count"] = division_count
        return context

# Class View untuk Model Project dari detail hingga delete
class ProjectView(ListView):
    model = Project
    template_name = 'data/table_project.html'
    ordering = ['start_date']
    project = Project.objects.all()
    

class AddProjectView(CreateView):
    model = Project
    template_name = 'function/add_project.html'
    form_class = PostForm
    success_url = reverse_lazy('home')

class UpdateProjectView(UpdateView):
    model = Project
    template_name = 'function/edit_project.html'
    form_class = PostForm
    success_url = reverse_lazy('project')

def delete(request, id):
    project = Project.objects.get(id=id)
    project.delete()
    return HttpResponseRedirect(reverse('project'))
    

# end comment

# Class View untuk Model Karyawan dari detail hingga delete
class AddEmployeeView(CreateView):
    model = Employee
    form_class = EmployeeForm
    template_name = 'function/add_employee.html'
    success_url = reverse_lazy('home')
    Employee.objects.get(user=1 )

# end Comment