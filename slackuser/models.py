from django.db import models

class SlackUser(models.Model):
    slackUsername = models.CharField(max_length=150, unique=True, verbose_name="slack username")
    backend = models.BooleanField(default=False)
    age = models.IntegerField()
    bio = models.TextField()
    
    def __str__(self):
        return self.username
    
    
class Student(models.Model):
    name = models.CharField(max_length=120, unique=True)
    DOB = models.DateField()
    BIO = models.TextField(blank=True)
    class StudentClass(models.TextChoices):
        PRIMARYONE = "PR1","Primary One"
        PRIMARYTWO = "PR2", "Primary Two"
        PRIMARYTHREE = "PR3", "Primary Three"
        
    studentClass = models.CharField(max_length=150, choices=StudentClass.choices, null=True)
    
    def __str__(self):
        return self.name
    
    
    
