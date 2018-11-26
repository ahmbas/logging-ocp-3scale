FROM docker.elastic.co/elasticsearch/elasticsearch:5.5.2
USER root
RUN chgrp -R 0 /usr/share/elasticsearch && \
    chmod -Rf g+rwx /usr/share/elasticsearch
USER elasticsearch
