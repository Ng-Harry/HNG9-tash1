from django.db import models

class SlackUser(models.Model):
    slack_username = models.CharField(max_length=150, unique=True, verbose_name="slack username")
    backend = models.BooleanField(default=False)
    age = models.IntegerField()
    bio = models.TextField()
    
    def __str__(self):
        return self.username
    
    
