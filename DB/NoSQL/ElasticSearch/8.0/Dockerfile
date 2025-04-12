FROM docker.elastic.co/elasticsearch/elasticsearch:8.9.0

USER root

RUN apt-get update && \
    apt-get install -y nano && \
    apt-get install -y wget

    rm -rf /var/lib/apt/lists/*

USER elasticsearch
