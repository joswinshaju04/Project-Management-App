from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import Project , Task


def login_page(request):
    if request.method == 'POST':
        a=request.POST.get('username')
        b=request.POST.get('password')
        c=authenticate(username=a, password=b)
        if c:
            login(request, c)
            return redirect('home')
        else:    
            return redirect('login')
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        a=request.POST.get('username')
        b=request.POST.get('email')
        c=request.POST.get('password')
        User.objects.create_user(username=a, email=b, password=c )
        return redirect('login')
    return render(request, 'register.html')
 
def home(request):
    items = Project.objects.filter(user=request.user).order_by('deadline')
    total_projects = items.count()
    active_projects = items.filter(status='Active').count()
    completed_projects = items.filter(status='Completed').count()

    return render(
        request,
        'home.html',
        {
            'items': items,
            'total_projects': total_projects,
            'active_projects': active_projects,
            'completed_projects': completed_projects,
        }
    )

def logout_user(request):
    logout(request)
    return redirect('login')

def create_project(request):
    if request.method == 'POST':
        a = request.POST.get('project_name')
        b = request.POST.get('description')
        c = request.POST.get('deadline')
        d = request.POST.get('status')

        Project.objects.create(
            project_name=a,
            description=b,
            deadline=c,
            status=d ,
            user=request.user
        )

        return redirect('home')
    return render(request, 'create_prj.html')

def add_task(request, id):

    project = Project.objects.get(id=id)

    if request.method == 'POST':

        task_name = request.POST.get('task_name')
        description = request.POST.get('description')
        status = request.POST.get('status')

        Task.objects.create(
            project=project,
            task_name=task_name,
            description=description,
            status=status
        )

        return redirect('home')

    return render(request, 'add_task.html', {'project': project})


def project_detail(request, id):

    project = Project.objects.get(id=id)

    tasks = Task.objects.filter(project=project)

    return render(
        request,
        'project_detail.html',
        {
            'project': project,
            'tasks': tasks
        }
    )


def delete_project(request, id):
    project = get_object_or_404(Project, id=id, user=request.user)

    if request.method == 'POST':
        project.delete()
        return redirect('home')

    return redirect('project_detail', id=id)


def delete_task(request, id):
    task = get_object_or_404(Task, id=id, project__user=request.user)

    project_id = task.project_id

    if request.method == 'POST':
        task.delete()
        return redirect('project_detail', id=project_id)

    return redirect('project_detail', id=project_id)