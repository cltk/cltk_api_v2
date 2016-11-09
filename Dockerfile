# Multithread Flask app with Gunicorn, then serve via Nginx

#FROM ubuntu:16.04
FROM python:3.5
MAINTAINER Kyle P. Johnson <kyle@kyle-p-johnson.com>

ENV DEBIAN_FRONTEND noninteractive
EXPOSE 80

RUN apt-get update
#RUN apt-get install -y python python-pip python-virtualenv nginx gunicorn supervisor git
RUN apt-get install -y nginx supervisor git

# Setup flask application
RUN mkdir -p /deploy/app
COPY app /deploy/app
COPY example.json /deploy/app
WORKDIR /deploy/app
RUN pip install --upgrade pip
RUN pip install gunicorn
RUN pip install -r requirements.txt

# Setup nginx
RUN rm /etc/nginx/sites-enabled/default
COPY flask.conf /etc/nginx/sites-available/
RUN ln -s /etc/nginx/sites-available/flask.conf /etc/nginx/sites-enabled/flask.conf
RUN echo "daemon off;" >> /etc/nginx/nginx.conf

# Setup supervisord
RUN mkdir -p /var/log/supervisor
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
COPY gunicorn.conf /etc/supervisor/conf.d/gunicorn.conf

# Get texts
#RUN git clone https://github.com/cltk/csel_openphilology_corpus.git
#WORKDIR ~/
#COPY install_corpora.py ~/
#RUN python3 install_corpora.py


# Start processes
CMD ["/usr/bin/supervisord"]
