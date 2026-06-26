from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):

    STATUS_CHOICES = [
        ('Active', 'Active'),
        ('On Hold', 'On Hold'),
        ('Completed', 'Completed'),
    ]

    project_name = models.CharField(max_length=100)
    description = models.TextField()
    deadline = models.DateField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Active'
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.project_name


class Task(models.Model):

    STATUS_CHOICES = [
        ('To Do', 'To Do'),
        ('In Progress', 'In Progress'),
        ('Done', 'Done'),
    ]

    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE
    )

    task_name = models.CharField(max_length=100)
    description = models.TextField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='To Do'
    )

    def __str__(self):
        return self.task_name        