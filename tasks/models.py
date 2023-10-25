from django.db import models

## from django.contrib.auth.models import User

class Task(models.Model):
  title = models.CharField(max_length=200)
  completed = models.BooleanField(default=False)

  def __str__(self):
    return self.title

class User(models.Model):
  username = models.CharField(max_length=200)
  password = models.CharField(max_length=200)

  def __str__(self):
    return self.username