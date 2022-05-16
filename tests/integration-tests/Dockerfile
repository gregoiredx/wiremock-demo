FROM python:3.10
COPY . ./tests
WORKDIR ./tests
RUN pip install -r requirements.txt
CMD pytest -v