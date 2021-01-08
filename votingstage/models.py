from django.db import models
from django.contrib.auth.models import User
from votingbooth.models import Election
from datetime import datetime

# Create your models here.

class ballot(models.Model):
    Election_Id = models.ForeignKey(Election, on_delete=models.CASCADE)
    Voter_Id = models.ForeignKey(User, on_delete=models.CASCADE)
    Hashed_vote = models.CharField(max_length=128)
    Date_voted = models.DateField(default=datetime.now, blank=True)

    def __str__(self):
        return self.Hashed_vote