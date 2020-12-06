from django.http import HttpResponse
from django.template import loader

from project.models import Project


def index(request):
    latest_project_list = Project.objects.order_by('-pub_date')[:3]
    template = loader.get_template('project/index.html')
    context = {
        'latest_project_list': latest_project_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request, project_id):
    return HttpResponse("You're looking at project %s." % project_id)