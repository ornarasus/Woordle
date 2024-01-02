FROM python:3.10-alpine
WORKDIR /usr/src/woordly
COPY . .
RUN apk update && apk upgrade && apk add bash && pip install aiogram
CMD ["python", "./run.py"]