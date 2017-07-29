############################################################
# Dockerfile to build NGINX + GUNICORN + DJANGO container images
# Based on Ubuntu
############################################################

FROM ubuntu:16.10
MAINTAINER Vacayo <dev@vacayo.com>


#--------------------------------------------------------------------------
# Patch OS and ENV
#--------------------------------------------------------------------------

# keep upstart quiet
RUN dpkg-divert --local --rename --add /sbin/initctl
RUN ln -sf /bin/true /sbin/initctl

# no tty
ENV DEBIAN_FRONTEND noninteractive


#--------------------------------------------------------------------------
# Install Packages
#--------------------------------------------------------------------------

# install python, nginx and supervisor
RUN apt-get update
RUN apt-get install -y \
    build-essential \
    libssl-dev \
    libffi-dev \
    python \
    python-dev \
    python-pip \
    python-tk \
    nginx \
    supervisor \
    postgresql-client \
    wget \
    git


#--------------------------------------------------------------------------
# Configure Services
#--------------------------------------------------------------------------

# stop supervisor and nginx service as we'll run it manually
RUN service supervisor stop
RUN service nginx stop

# install configurations for nginx and supervisord
ADD deployment/supervisord.conf /etc/supervisor/conf.d/
ADD deployment/nginx.conf /etc/nginx/nginx.conf

# install python dependencies
RUN mkdir /opt/app
ADD requirements.txt /opt/app
RUN pip install --upgrade pip
RUN pip install -r /opt/app/requirements.txt

# install app
COPY . /opt/app
#RUN cd /opt/app && ./manage.py collectstatic --noinput
#RUN chown -R www-data:www-data /opt/app


#--------------------------------------------------------------------------
# Run Services
#--------------------------------------------------------------------------

EXPOSE 80
ENTRYPOINT supervisord
