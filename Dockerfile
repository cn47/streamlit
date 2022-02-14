FROM python:3.10.2-slim-buster

RUN apt-get update && apt-get install -y --no-install-recommends \
        curl \
        locales \
        less \
        vim \
        wget \
    && localedef -f UTF-8 -i ja_JP ja_JP.UTF-8 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /tmp
COPY requirements.txt /tmp

RUN pip install --upgrade \
        pip \
        setuptools \
    && pip install -r requirements.txt \
    && rm -rf ${HOME}/.pip/cache
