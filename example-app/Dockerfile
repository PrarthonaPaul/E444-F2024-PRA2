FROM python:3.11-slim

WORKDIR /example-app

COPY . /example-app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 5000

ENV FLASK_APP=hello.py
ENV FLASK_ENV=development

CMD ["flask", "run", "--host=0.0.0.0"]