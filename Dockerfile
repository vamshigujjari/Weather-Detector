FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get install -y python3-pip python3-dev build-essential libpng-dev libjpeg-dev python 

COPY requirements.txt /app/
WORKDIR /app
RUN pip3 install -r requirements.txt

COPY weather_model_4.pth /app/weather_model_4.pth
COPY app.py /app/
COPY CNN_Model.py /app/
COPY templates /app/templates
COPY static /app/static

ENTRYPOINT ["python3"]
CMD ["app.py"]
