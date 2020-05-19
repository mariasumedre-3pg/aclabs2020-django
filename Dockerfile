FROM python:3.7

RUN pip install Django==2.2.12
RUN pip install graphene_django==2.8.2

RUN mkdir /app
ADD . /app
WORKDIR /app

CMD [ "python", "aclabs/manage.py", "runserver", "0:8000"]
