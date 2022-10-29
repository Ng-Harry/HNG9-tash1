from django.db import models

class SlackUser(models.Model):
    username = models.CharField(max_length=150, unique=True, verbose_name="slack username")
    backend = models.BooleanField(default=False)
    age = models.IntegerField()
    bio = models.TextField()
    
