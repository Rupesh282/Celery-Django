from django.db import models

# Create your models here.


class TaskResult(models.Model):
    STATS = (
        ("PENDING", "PENDING"),
        ("SUCCESS", "SUCCESS"),
        ("STARTED", "STARTED"),
        ("FAILURE", "FAILURE"),
        ("RETRY", "RETRY"),
        ("REVOKED", "REVOKED"),
    )
    task_id = models.CharField(max_length=191)
    task_name = models.CharField(max_length=100)
    task_status = models.CharField(max_length=100, choices=STATS)
    

    def __str__(self):
        return self.task_name + "_" + self.task_status