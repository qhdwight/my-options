from django.db import models

class Scholarship(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField()
    description = models.CharField(max_length=500)
    deadlineMonth = models.PositiveSmallIntegerField()
    deadlineDay = models.PositiveSmallIntegerField()
    amount = models.PositiveIntegerField()
    upperAmount = models.PositiveIntegerField(null=True)