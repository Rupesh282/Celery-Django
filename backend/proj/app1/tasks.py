# Create your tasks here

from celery import shared_task
from time import sleep


@shared_task
def add(x, y):
    sleep(50)
    return x + y


@shared_task
def mul(x, y):
    sleep(30)
    return x * y / 0