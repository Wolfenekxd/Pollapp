from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Election(models.Model):
    Question = models.TextField(max_length=256)
    Start_date = models.DateField()
    End_date = models.DateField()
    Owner_Id = models.ForeignKey(User, on_delete=models.CASCADE)
    objects = models.Manager()

    def __str__(self):
        return self.Question

class Answers(models.Model):
    Election_Id = models.ForeignKey(Election, on_delete=models.CASCADE)
    Answer = models.CharField(max_length=64)
    Result = models.IntegerField(default=0)
    Answer_date = models.DateField()
    objects = models.Manager()

    def __str__(self):
        return self.Answer