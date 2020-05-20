FROM python:3.7

RUN apt update
RUN apt-get install nginx -y

RUN pip install Django==2.2.12
RUN pip install graphene_django==2.8.2

RUN pip install gunicorn

COPY configuration/aclabs /etc/nginx/sites-available/
RUN ln -s /etc/nginx/sites-available/aclabs /etc/nginx/sites-enabled

RUN mkdir /app
ADD . /app
WORKDIR /app


CMD [ "configuration/entrypoint.sh" ]
