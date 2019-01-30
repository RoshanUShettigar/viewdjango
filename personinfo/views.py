from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .models import PersonApp
from .models import Department
from django.urls import reverse_lazy

# Create your views here.

class IndexView(generic.ListView):
    template_name = 'personinfo/index.html'
    context_object_name = 'PInfo'

    def get_queryset(self):
        return PersonApp.objects.all()
    def get_queryset(self):
        return Department.objects.all()


class Infosave(CreateView):
    model = PersonApp
    fields = ['fname', 'lname', 'phone_no', 'email', 'city']

class editInfo(UpdateView):
    model = PersonApp
    fields = ['fname', 'lname', 'phone_no', 'email', 'city']

class deleteInfo(DeleteView):
    model = PersonApp
    success_url = reverse_lazy('personinfo:index')
