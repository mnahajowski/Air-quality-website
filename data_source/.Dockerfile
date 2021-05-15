FROM python:3.9

ADD ./requirements.txt /app/requirements.txt
ENV PYTHONPATH="${PYTHONPATH}:/app"
ENV TZ="Europe/Warsaw"

RUN pip install -r /app/requirements.txt

RUN apt-get update \
    && apt-get install -y x11vnc xvfb fluxbox wget wmctrl \
    && apt-get clean

RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list

RUN apt-get update && apt-get install -y google-chrome-stable

ADD src/ /app

CMD python /app/main.py
