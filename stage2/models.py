from django.db import models

class Calc(models.Model):
    x = models.IntegerField()
    y = models.IntegerField()
    class operationType(models.TextChoices):
        addition = 'addition','addition'
        subtraction = 'subtraction', 'subtraction'
        multiplication = 'multiplication', 'multiplication'
    operation_type = models.CharField(max_length=200, choices=operationType.choices)
