from django.db import models

# Create your models here.


class Leaders(models.Model):
    playerNum = models.IntegerField(default=10)
