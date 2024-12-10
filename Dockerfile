FROM python:3.10

WORKDIR /app

COPY main.py /app/main.py
WORKDIR /app

RUN pip install --no-cache-dir -r requirements.txt

CMD [ "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000" ]