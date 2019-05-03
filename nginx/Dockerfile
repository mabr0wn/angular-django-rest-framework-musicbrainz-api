FROM nginx
RUN apt-get update && apt-get install vim curl -y

ADD ./proxy/conf.d/default.conf /etc/nginx/conf.d/default.conf