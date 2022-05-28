from django.db import models

# Create your models here.

status_choices = (("Pending", "Pending"), ("Done", "Done"), ("Deleted", "Deleted"))

class Todo(models.Model):

    task = models.CharField(max_length=100)
    responsible = models.CharField(max_length=100)
    description = models.CharField(max_length=10000)
    task_creation_date = models.DateField()
    wished_due_date = models.DateField()
    estimated_duration = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=status_choices, default="Pending")
    active = models.BooleanField(default=1)

    def __str__(self):
        return f'{self.task} - {self.responsible} - {self.description} - {self.task_creation_date} - ' \
               f'{self.wished_due_date} - {self.estimated_duration}'
