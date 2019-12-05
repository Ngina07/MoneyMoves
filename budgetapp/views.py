from django.shortcuts import render

# Create your views here.
def project_list(request):
    return render(request,'project-list.html')

def project_detail(request,project_slug):
    # Fetch one budget
    return render(request,'project-detail.html')