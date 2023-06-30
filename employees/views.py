from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render
from django.urls import reverse_lazy

from .forms import EmpForm
from .models import Employees


class TmListView(ListView):
    model = Employees
    template_name = 'home.html'

class TableListView(ListView):
    model = Employees
    template_name = 'table.html' 

class EmpCreateView(CreateView):
    model = Employees
    template_name = 'profile.html'
    fields = '__all__'

class EmpUpdView(UpdateView):
    model = Employees
    fields = ['work_time','productivity']
    template_name = 'upd.html'

class EmpDelView(DeleteView):
    model = Employees
    template_name = 'del.html'
    success_url = reverse_lazy('table')