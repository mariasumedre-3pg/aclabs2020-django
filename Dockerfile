FROM python:3.7

RUN pip install Django==2.2.12

RUN mkdir /app
ADD . /app
WORKDIR /app

CMD [ "python", "aclabs/manage.py", "runserver", "0:8000"]