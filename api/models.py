from django.db import models
from django.utils import timezone

from uuid import uuid4

# Create your models here.

class List(models.Model):
    uuid = models.CharField(max_length=50, unique=True, primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=200, default='New list')

    @classmethod
    def create(cls, title = 'New list'):
        list = cls(uuid = str(uuid4())[:8], title=title)

        return list

    def update_title(self, title):
        self.title = title
        self.save()

    def add_task(self, title, completed=False):
        return Task.objects.create(title=title, completed=completed, list=self)

    def delete_task(self, task):
        task.delete()

    def get_tasks(self):
        return Task.objects.filter(list=self)

    def __str__(self):
        return self.title + ' (' + self.uuid + ')'

class Task(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True) 
    list = models.ForeignKey(List, on_delete=models.CASCADE)

    class Meta:
        ordering = ['updated_at']

    def toggle_completed(self):
        self.completed = not self.completed
        self.save()

    def update_title(self, title):
        self.title = title
        self.save()

    def get_list(self):
        return self.list

    def __str__(self):
        return self.title