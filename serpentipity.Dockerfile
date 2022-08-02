FROM python:slim

WORKDIR /app

COPY src/*.py .

RUN pip install flask

CMD ["python", "main.py"]

