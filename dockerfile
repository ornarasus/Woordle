FROM python:3.10-alpine
WORKDIR /root/woordly
COPY . .
RUN pip install aiogram
RUN pip install lxml
CMD ["python", "/root/woordly/run.py"]
