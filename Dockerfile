# Pull official base image
FROM python:3.6

# set work direcotory
WORKDIR /code

# Python specific Environment Variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -f -y postgresql-client
COPY Pipfile Pipfile.lock ./
RUN pip install --upgrade pip
RUN pip install pipenv
RUN pipenv install --system --deploy
COPY . /code/

ENTRYPOINT [ "/code/entrypoint.sh" ]