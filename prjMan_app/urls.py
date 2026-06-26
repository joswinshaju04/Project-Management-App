from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_page, name='login'),
    path('register/', views.register, name='register'),
    path('home/', views.home, name='home'),
    path('logout/', views.logout_user, name='logout'),
    path('create-project/', views.create_project, name='create_project'),
    path(
    'add_task/<int:id>/',
    views.add_task,
    name='add_task'),
    path(
        'project/<int:id>/',
        views.project_detail,
        name='project_detail'
    ),
    path(
        'project/<int:id>/delete/',
        views.delete_project,
        name='delete_project'
    ),
    path(
        'task/<int:id>/delete/',
        views.delete_task,
        name='delete_task'
    ),
]