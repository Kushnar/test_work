from django.shortcuts import render
from django_celery_beat.models import PeriodicTask, CrontabSchedule
from rest_framework.generics import ListAPIView, UpdateAPIView, ListCreateAPIView
from rest_framework.views import APIView, Response
from rest_framework.status import HTTP_200_OK

from main.models import Weather
from main.serializers import WeatherSerializer, ChangeUpdateTimeSerializer
from main.tasks import run_parser


# API endpoint for manual upd weather
class GetWeatherDataAPIView(ListAPIView):
    queryset = Weather.objects.all()
    serializer_class = WeatherSerializer

    def post(self, request):
        run_parser.delay()
        return Response(data={'result': 'running task...'}, status=HTTP_200_OK)


# API endpoint for changing hours of auto getting weather
class ChangeUpdateTimeAPIView(APIView):
    queryset = PeriodicTask.objects.all()
    serializer_class = ChangeUpdateTimeSerializer

    def put(self, request):
        serializer = ChangeUpdateTimeSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'msg': 'Success'})
        return Response({'msg': 'Something goes wrong'})
