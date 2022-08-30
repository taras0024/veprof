FROM python:3.9

RUN apt update
RUN apt-get update

RUN mkdir veprof

COPY ./requirements.txt /veprof
RUN pip install --upgrade pip
RUN pip install -r ./veprof/requirements.txt --ignore-installed --force-reinstall --upgrade --no-cache-dir

COPY . /veprof
WORKDIR /veprof

EXPOSE 8000
