FROM php:7.1-apache

# Install Composer
RUN curl -sS https://getcomposer.org/installer | php \
  && mv composer.phar /usr/local/bin/composer \
  && chmod +x /usr/local/bin/composer

RUN apt-get update \
  && apt-get install -y bash git \
  && rm -rf /var/lib/apt/lists/* \
  && apt-get autoremove -y \
  && apt-get clean


# selfoss requirements: mod-headers, mod-rewrite, gd
RUN a2enmod headers rewrite && \
    apt-get update && \
    apt-get install -y unzip libjpeg62-turbo-dev libpng12-dev libpq-dev && \
    docker-php-ext-configure gd --with-jpeg-dir=/usr/include/ && \
    docker-php-ext-install gd mbstring pdo_pgsql pdo_mysql


RUN git clone https://github.com/SSilence/selfoss.git /var/www/html/

RUN chown -R www-data:www-data /var/www/
RUN su www-data -s /bin/bash -c "cd /var/www/html/ && composer require 'j0k3r/graby'"


RUN a2enmod rewrite

RUN chown -R www-data:www-data /var/www/