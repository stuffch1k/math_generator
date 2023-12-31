FROM python:3.11

RUN mkdir /generator_app

WORKDIR /generator_app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

# RUN alembic updarge head
RUN chmod a+x docker/*.sh
# WORKDIR src

# CMD gunicorn main:app --workers 1 --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:8000