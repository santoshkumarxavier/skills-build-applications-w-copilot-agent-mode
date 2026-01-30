from django.db import models
from django.conf import settings

# Create your models here.


class Activity(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='activities')
    activity_type = models.CharField(max_length=100)
    duration_minutes = models.PositiveIntegerField()
    distance_km = models.FloatField(null=True, blank=True)
    date = models.DateField()

    def __str__(self):
        return f"{self.user} - {self.activity_type} on {self.date}"
