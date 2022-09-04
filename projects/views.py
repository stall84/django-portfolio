import http
from django.shortcuts import render
from projects.models import Projects
# Create your views here.


def all_projects(request):

    # Query DB for all project objects
    # utilize the ORM aspect of Django
    projects = Projects.objects.all()
    # Notice below in the return we include a 3rd argument (a dictionary) which we keyed
    # for our projects object. What this will do is along with the HttpRequest, the database queried object
    # will be 'forwarded' with every request / page-hit, making the db objects accessible and renderable from
    # the included template.
    return render(request, 'projects/all_projects.html', {
        'projects': projects
    })


def project_list(request):

    return render(request, 'projects/projects_list.html')
