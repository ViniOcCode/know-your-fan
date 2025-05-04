FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt torch==2.7.0+cpu torchvision==0.22.0+cpu -f https://download.pytorch.org/whl/torch_stable.html

COPY . .

EXPOSE 5000

CMD [ "python", "./main.py" ]
