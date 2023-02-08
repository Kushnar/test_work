from django.db import models


class Weather (models.Model):
    date = models.DateField(unique=True)
    temperature = models.IntegerField()
    weather_description = models.CharField(max_length=150)

    class Meta:
        ordering = ('-date',)
