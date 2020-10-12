FROM python:3.7.0-stretch
ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt
RUN ["python", "main.py", "2"]