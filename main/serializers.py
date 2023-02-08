from django_celery_beat.models import CrontabSchedule, PeriodicTask
from rest_framework.serializers import ModelSerializer
from main.models import Weather


class WeatherSerializer(ModelSerializer):

    class Meta:
        model = Weather
        exclude = ('id',)


class ChangeUpdateTimeSerializer(ModelSerializer):

    class Meta:
        model = CrontabSchedule
        fields = ('hour',)

    def save(self, **kwargs):
        crontab_id = PeriodicTask.objects.get(name='GetWeather').crontab.id
        obj = CrontabSchedule.objects.get(id=crontab_id)
        obj.hour = self.data.get('hour')
        obj.save()
        return obj
