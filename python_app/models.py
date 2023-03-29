from django.db import models

# Create your models here.
class conn(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    id = models.IntegerField

    class meta:
        db_table = 'conn'