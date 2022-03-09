# Pull base image - Almost never changes

FROM python:3.10.2

# Set environmental variables

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBUG 0

# Set work directory

WORKDIR /code

# Install dependancies

COPY Pipfile Pipfile.lock /code/
RUN pip install pipenv && pipenv install --system

#Copy project 

COPY . /code/

# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

# collect static files
RUN python manage.py collectstatic --noinput

# run gunicorn
CMD gunicorn taskList_project.wsgi:application --bind 0.0.0.0:$PORT


