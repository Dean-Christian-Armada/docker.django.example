FROM python:2.7

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/
COPY gunicorn_conf.py /usr/src/app/
COPY project/. /usr/src/app

RUN pip install --no-cache-dir -r requirements.txt

CMD ["gunicorn", "-c", "gunicorn_conf.py", "project.wsgi:application", "--reload"]