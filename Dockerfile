FROM python:3.12-slim

RUN apt-get update && apt-get install -y poppler-utils

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt -f https://download.pytorch.org/whl/torch_stable.html

COPY . .

EXPOSE 5000

CMD [ "gunicorn", "main:app", "--bind", "0.0.0.0:5000" ]
