FROM node:22.16-bullseye AS base

RUN apt-get update && apt-get install -y \
 python3 \
    python3-pip \
    python3-venv \
    && apt-get clean

WORKDIR /WIENER/app

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY . .

RUN npm install

RUN npx tailwindcss -i ./app/static/src/tailwind.css -o ./app/static/css/main.css --minify


EXPOSE 5000

CMD [ "python3", "app/main.py"]



