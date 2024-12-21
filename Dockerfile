FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt flask

EXPOSE 8000

CMD [ "python", "server.py" ]