from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .models import Assignment
from .forms import AssignmentForm


# Create your views here.
def home_view(request):
    pass


class AssignmentCreateView(CreateView):
    model = Assignment
    form_class = AssignmentForm
    success_url = reverse_lazy('assignment-create')
    template_name = 'assignment/create.html'

    # def form_valid(self, form):
    #      import pdb;pdb.set_trace()
    #      return super().form_valid(form)