FROM python:3.6-slim-buster
WORKDIR /usr/src/app
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt
COPY ./Flask-app.py /usr/src/app/
EXPOSE 5000
ENTRYPOINT ["python", "Flask-app.py"]