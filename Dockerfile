FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /spa_table
EXPOSE 8000
WORKDIR /cargo

COPY ./requirements.txt /cargo/
COPY . /cargo

RUN pip3 install -r requirements.txt --no-cache-dir





