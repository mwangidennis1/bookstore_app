# I need the base image 
FROM python:3.10

#env variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# I need the work directory
WORKDIR /books

# I need  my dependancies
COPY Pipfile Pipfile.lock /books/
RUN pip install pipenv && pipenv install --system

#Copy project
COPY . /books/