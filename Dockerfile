FROM python:3.10
COPY ./requirements.txt .
RUN pip install -r requirements.txt
RUN mkdir app
WORKDIR ./app
COPY app.py .
CMD flask run --host 0.0.0.0 --port 80