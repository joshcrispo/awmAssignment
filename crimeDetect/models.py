from django.contrib.gis.db import models
from django.utils import timezone


class Location(models.Model):
    coordinates = models.PointField()
    comment = models.TextField(default='')
    log_date = models.DateTimeField(default=timezone.now, blank=True)

    def __str__(self):
        return f"{self.coordinates} - {self.comment} - {self.log_date}"
