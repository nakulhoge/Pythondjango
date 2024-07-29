# models.py

from django.db import models



class Registration(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

class Login(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)


class Election(models.Model):
    title = models.CharField(max_length=100)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __str__(self):
        return self.title

class Candidate(models.Model):
    election = models.ForeignKey(Election, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    party_name = models.CharField(max_length=100)
    symbol = models.ImageField(upload_to='candidate_symbols/')
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Vote(models.Model):
    election = models.ForeignKey(Election, on_delete=models.CASCADE)
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    voted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Vote for {self.candidate} in {self.election}'

