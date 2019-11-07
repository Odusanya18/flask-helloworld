FROM python:2.7

COPY requirements.txt requirements.txt
COPY app.py app.py

ENV http_proxy=http://172.25.30.117:6060
ENV https_proxy=http://172.25.30.117:6060

RUN pip install -r requirements.txt --proxy 172.25.30.117:6060

COPY ./harden.sh .
RUN chmod +x harden.sh && \
    sh harden.sh && \
    rm harden.sh

ENV http_proxy=
ENV https_proxy=

USER helloworld

EXPOSE 80
ENTRYPOINT [ "python", "app.py" ]

#docker run -it — cpus 1 — memory 512Mb helloworld
