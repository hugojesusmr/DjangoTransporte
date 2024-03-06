FROM python:3.12-alpine

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


RUN apk update \
    && apk add --no-cache gcc musl-dev mysql-dev python3-dev libffi-dev \
    && pip install --upgrade pip

COPY ./requirements.txt /code/requirements.txt
RUN pip install -r /code/requirements.txt
COPY . /code/
WORKDIR /code/

# ENV DB_HOST=$DB_HOST
# ENV DB_NAME=$DB_NAME
# ENV DB_USER=$DB_USER
# ENV DB_PASSWORD=$DB_PASSWORD
# ENV DB_PORT=$DB_PORT

# RUN python manage.py collectstatic 
# RUN python manage.py makemigrations 
# RUN python manage.py migrate 
CMD ["sh","entrypoint.sh"]    
#CMD exec gunicorn core.wsgi:application --bind 0.0.0.0:8000 --workers 3
