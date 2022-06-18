from django.db import models
from django.contrib.auth.models import User

class Company(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to = 'image')
    description = models.TextField()
    vote = models.ManyToManyField(User,default=0, blank=True, related_name='companies_vote')
    date = models.DateTimeField()

    def __str__(self):
        return self.name
