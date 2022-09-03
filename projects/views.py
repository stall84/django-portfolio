import http
from django.shortcuts import render
from projects.models import Projects
# Create your views here.


def all_projects(request):

    return render(request, 'projects/all_projects.html')


def project_list(request):

    return render(request, 'projects/projects_list.html')
