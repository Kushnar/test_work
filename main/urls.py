from django.urls import path

from main import views
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Weather API')

urlpatterns = [
    path('', schema_view),
    path('api/weather/', views.GetWeatherDataAPIView.as_view()),
    path('api/change-time/', views.ChangeUpdateTimeAPIView.as_view())
]
