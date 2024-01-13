FROM python:3.10-alpine
WORKDIR /root/woordly
COPY . .
RUN apk update
RUN apk add --no-cache bash
RUN pip install aiogram
ENTRYPOINT ["/root/woordly/run.py"]
