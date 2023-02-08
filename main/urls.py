from django.urls import path

from main import views


urlpatterns = [
    path('api/weather/', views.GetWeatherDataAPIView.as_view()),
    path('api/change-time/', views.ChangeUpdateTimeAPIView.as_view())
]
