FROM ubuntu:latest

MAINTAINER yoyo koyo yoyokoyo.contact@gmail.com

RUN apt-get update
RUN apt-get install apt-utils systemd apache2 python python-pip jq git libapache2-mod-wsgi python-dev wget nano -y


WORKDIR /var/www/
RUN rm -rf html
RUN git clone https://github.com/yoyokoyo/yoyokoyo.git
RUN chmod a+x yoyokoyo/bash.sh yoyokoyo/__init__.py
RUN a2enmod wsgi
#RUN pip install virtualenv
#RUN virtualenv venv
#RUN /bin/bash -c "source venv/bin/activate"
RUN pip install Flask

WORKDIR /var/www/yoyokoyo/
#RUN /bin/bash -c "deactivate"
RUN echo "3.121.151.8 yoyokoyo.com" >> /etc/hosts
RUN mv /var/www/yoyokoyo/apache2/yoyokoyo.com.conf /etc/apache2/sites-available/yoyokoyo.com.conf

##LETS ENCRYPT PART TO GET KEYS
RUN openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /etc/ssl/private/apache-selfsigned.key -out /etc/ssl/certs/apache-selfsigned.crt -subj "/C=US/ST=Florida/L=Toulouse/O=Company/OU=IT/CN=yoyokoyo.com"
RUN openssl dhparam -out /etc/ssl/certs/dhparam.pem 2048
##LETS ENCRYPT PART TO GET KEYS

RUN mkdir -p /var/www/yoyokoyo.com/logs
RUN a2dissite 000-default
RUN a2ensite yoyokoyo.com.conf
RUN chown -R www-data:www-data /var/www/yoyokoyo.com

RUN ./bash.sh &
RUN /etc/init.d/apache2 restart

EXPOSE 80 443
