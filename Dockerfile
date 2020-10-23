# Pull official base image
FROM python:3.6

# set work direcotory
WORKDIR /code

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY Pipfile Pipfile.lock ./
RUN pip install --upgrade pip
RUN pip install pipenv
RUN pipenv install --system --deploy
COPY ./entrypoint.sh .
COPY . ./
EXPOSE 8000

ENTRYPOINT [ "/code/entrypoint.sh" ]