from celery import Celery
from time import sleep



app = Celery()


@app.task
def add(x, y):
    sleep(30)
    return x + y
