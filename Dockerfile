FROM python:3.10-alpine
WORKDIR /root/woordle
COPY . .
RUN pip install aiogram
RUN pip install lxml
CMD ["python", "run.py"]
