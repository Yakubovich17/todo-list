FROM python:3.12

WORKDIR /code

COPY requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 50505

ENTRYPOINT ["gunicorn", "--config", "gunicorn.conf.py", "run:app"]