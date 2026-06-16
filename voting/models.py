from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import User

class Voter(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    usn = models.CharField(max_length=20, unique=True)
    photo = models.ImageField(upload_to='voter_photos/')

    def __str__(self):
        return f"{self.user.username} - {self.usn}"
class Candidate(models.Model):
    name = models.CharField(max_length=100)

    contesting_for = models.CharField(
        max_length=100,
        verbose_name="Contesting For"
    )

    def __str__(self):
        return self.name

class Vote(models.Model):

    voter = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    candidate = models.ForeignKey(
        Candidate,
        on_delete=models.CASCADE
    )

    voted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.voter.username} voted for {self.candidate.name}"
class ElectionResult(models.Model):

    result_declared = models.BooleanField(default=False)

    def __str__(self):
        return "Election Result Status"