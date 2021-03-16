# from django.shortcuts import render
from django.views import generic

from .models import Projects

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'projects/index.html'
    context_object_name = 'all_projects'

    def get_queryset(self):
        return Projects.objects.all()

class DetailView(generic.DetailView):
    model = Projects
    template_name = 'projects/details.html'