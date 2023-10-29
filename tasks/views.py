from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Task, User
import sqlite3

user = None

def index(request):
  return HttpResponse("Hello, world. You're at the tasks index.")

@csrf_exempt
def task_list(request):
  global user
  tasks = Task.objects.all()
  if request.method == 'GET':
    return render(request, 'tasks/task_list.html', {'tasks': tasks, 'user': user})
  if request.method == 'POST':
    Task.objects.create(title=request.POST['title'])
  return render(request, 'tasks/task_list.html', {'tasks': tasks, 'user': user})

def search(request):
  if request.method == 'POST':
    query = request.POST['title']
    connection = sqlite3.connect('db.sqlite3')
    cursor = connection.cursor()
    tasks = cursor.execute("SELECT title FROM tasks_task WHERE title LIKE '%" + query + "%'").fetchall()
    ## tasks = Task.objects.filter(title__contains=request.POST['title'])
  return render(request, 'tasks/task_list.html', {'tasks': tasks})

def profile(request, user_id):
  global user
  find = User.objects.filter(id=user_id).first()
  ## if request.user.id == user_id:
  ##   user = User.objects.filter(id=user_id).first()
  ##   return render(request, 'tasks/profile.html', {'user': user})
  ## else:
  ##   return HttpResponseForbidden("You are not authorized to view this page")

  return render(request, 'tasks/profile.html', {'user': find})


@csrf_exempt
def login(request):
  if request.method == 'GET':
    return render(request, 'tasks/login.html')
  if request.method == 'POST':
    global user
    user = User.objects.filter(username=request.POST['username'], password=request.POST['password']).first()
    if user:
      return redirect('/task_list', user=user )
    else:
      return render(request, 'tasks/login.html', {'error': 'Invalid username or password'})
  return render(request, 'tasks/task_list.html')

@csrf_exempt
def register(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']
    password2 = request.POST['password2']
    ##if username == '' or password == '':
    ##  return render(request, 'tasks/register.html', {'error': 'Username or password cannot be empty'})
    ##elif username == password:
    ##  return render(request, 'tasks/register.html', {'error': 'Username and password cannot be the same'})
    ##elif username == 'admin':
    ##  return render(request, 'tasks/register.html', {'error': 'Username cannot be admin'})
    ##elif len(password) < 8:
    ##  return render(request, 'tasks/register.html', {'error': 'Password must be at least 8 characters'})
    ##elif not any(char.isdigit() for char in password):
    ##  return render(request, 'tasks/register.html', {'error': 'Password must contain at least one number'})
    ##elif not any(char.isupper() for char in password):
    ##  return render(request, 'tasks/register.html', {'error': 'Password must contain at least one uppercase letter'})
    ##elif not any(char.islower() for char in password):
    ##  return render(request, 'tasks/register.html', {'error': 'Password must contain at least one lowercase letter'})
    ##elif password in ['password', 'Password', '12345678', 'qwertyuiop', 'asdfghjkl', 'zxcvbnm']:
    ##  return render(request, 'tasks/register.html', {'error': 'Password is too common'})
    ##elif username in ['admin', 'root', 'administrator']:
    ##  return render(request, 'tasks/register.html', {'error': 'Username is too common'})
    ##if password != password2:
    ##  return render(request, 'tasks/register.html', {'error': 'Passwords do not match'})
    user = User.objects.filter(username=request.POST['username']).first()
    if user:
      return render(request, 'tasks/register.html', {'error': 'Username already exists'})
    else:
      User.objects.create(username=request.POST['username'], password=request.POST['password'])
      ## User.objects.create_user(username=request.POST['username'], password=request.POST['password'])
      return render(request, 'tasks/register.html', {'error': 'User created'})
  return render(request, 'tasks/register.html')

def logout(request):
  global user
  user = None
  return redirect('/task_list')
