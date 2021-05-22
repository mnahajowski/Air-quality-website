FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

ADD ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

COPY ./src /app
