FROM python:3.11

WORKDIR /app
RUN pip install django

COPY . .

EXPOSE 8080

ENV DJANGO_SETTINGS_MODULE=simplon.settings
ENV DATABASE8URL=sqlite:///db.sqlite3


RUN python manage.py migrate

#RUN python manage.py collectstatic --noinput

CMD ["python","manage.py","runserver","12700.1:8000"]