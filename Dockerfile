FROM python:3.8
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8000
#CMD gunicorn -c gunicorn_conf.py flask_mmk:app
CMD python flask_mmk.py
