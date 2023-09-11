from django.db import models


# Create your models here.
class Notification(models.Model):
    data_id = models.CharField(max_length=11)
    action = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)
    type = models.CharField(max_length=100)

    def __str__(self):
        return self.data_id + " - " + self.date_created.strftime("%d/%m/%Y %H:%M:%S")
