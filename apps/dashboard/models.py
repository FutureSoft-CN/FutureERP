from django.db import models

# Create your models here.
class modules_manager(models.Model):
    userid = models.IntegerField(unique=True)