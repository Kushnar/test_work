FROM joyzoursky/python-chromedriver:latest



ENV PYTHONDONTWRIGHTBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/weather

COPY ./req.txt /usr/src/req.txt
RUN pip install -r /usr/src/req.txt

COPY . /usr/src/weather
