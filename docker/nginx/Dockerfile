FROM nginx:latest

COPY etc/nginx/* /etc/nginx/conf.d/
ADD entrypoint.sh /opt/entrypoint.sh

RUN set -x \
  && apt-get update \
  && apt-get upgrade -y --no-install-recommends \
  && apt-get install -y openssl

RUN chmod a+x /opt/entrypoint.sh
RUN /bin/bash -c "source /opt/entrypoint.sh /etc/letsencrypt/live/ssl_keys localhost"
