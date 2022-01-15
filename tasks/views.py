# Add all your views here
from django.shortcuts import render
from django.http import HttpResponseRedirect

tasks = []
completed_tasks = []

def view_tasks(requests):
		return render(requests, "tasks.html", {"tasks": tasks})

def add_task(requests):
		task = requests.GET.get("task")
		tasks.append(task)
		return HttpResponseRedirect("/tasks")

def delete_task(requests, id):
		del tasks[id-1]
		return HttpResponseRedirect("/tasks")

def complete_task(requests, id):
		task = tasks.pop(id-1)
		completed_tasks.append(task)
		return HttpResponseRedirect("/tasks")

def list_complete_task(requests):
		return render(requests, "completed_tasks.html", {"tasks": completed_tasks})
