# Multithread Flask app with Gunicorn, then serve via Nginx

# use Python with `RUN python3 <>.py`
FROM python:3.5
MAINTAINER Kyle P. Johnson <kyle@kyle-p-johnson.com>

ENV DEBIAN_FRONTEND noninteractive
EXPOSE 80

RUN apt-get update
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
RUN ~/
RUN mkdir -p ~/cltk_data/corpora/
RUN git clone --depth 1 https://github.com/cltk/capitains_text_corpora.git


# Start processes
CMD ["/usr/bin/supervisord"]
