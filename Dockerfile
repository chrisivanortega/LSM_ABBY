
FROM python:3
ENV PYTHOBUFFERED=1
WORKDIR /code/
COPY requirements.txt /code/requirements.txt
RUN pip install -r requirements.txt
COPY . /code/

