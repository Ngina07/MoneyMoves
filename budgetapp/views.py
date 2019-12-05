from django.shortcuts import render,get_object_or_404
from .models import *
from django.views.generic import CreateView

# Create your views here.
def project_list(request):
    return render(request,'project-list.html')

def project_detail(request,project_slug):
    # Fetch one budget
    project = get_object_or_404(Project, slug=project_slug)
    

    return render(request,'project-detail.html',{'project': project, 'expense_list':project.expenses.all()})


class ProjectCreateView(CreateView):
    model = Project
    template_name = 'add-project.html'
    fields = ('name', 'budget')

