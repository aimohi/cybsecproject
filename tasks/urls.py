from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('task_list/', views.task_list, name='task_list'),
  path('search/', views.search, name='search'),
  path('login/', views.login, name='login'),
  path('register/', views.register, name='register'),
  path('logout/', views.logout, name='logout'),
  path('profile/', views.profile, name='profile'),
  path('profile/<user_id>/', views.profile, name='profile')
]