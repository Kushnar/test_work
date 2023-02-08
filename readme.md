# Weather Test App

## About app

This app is a Django-Based web application, which automatically updates weather data and allows to user to get weather
in Kyiv for today and next 5 days via
API endpoints. Basically app updates data every day at 9 a.m., but users can set custom time of running GetWeather
process by setting their own time using API endpoints or run that task manually at the same way

## Technologies

- Django == 4.1.6
- DjangoRestFramework == 3.14.0
- Django-Rest-Swagger == 2.2.0
- Celery == 5.2.7
- Redis==4.4.2
- Selenium==4.8.0

## API-endpoints
- docs: [http://localhost:8000](http://localhost:8000)
- (GET) api/weather: get weather list 
- (POST) api/weather: run manual updating of weather data (without Post-data)
- (PUT) api/change-time/ : require hour(s) argument from 0 to 23, to set hour of starting auto-getting weather data

## Installation

This app requires [Docker](https://www.docker.com/) to run docker container.

1. Clone this repo and after run your Docker

```sh
 git clone https://github.com/Kushnar/test_work.git
```

2. Build container from existed docker-compose.yml file (you should run command from the same directory with
   docker-compose.yml )

```sh
 docker-compose build
```

3. Run the container (you should run command from the same directory with
   docker-compose.yml )

```sh
 docker-compose up
```

4. Your app will run at [http://localhost:8000/](http://localhost:8000/) on your host machine and index page will be
   shown as API documentation


