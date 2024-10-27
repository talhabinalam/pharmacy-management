from django.db import models

class Medicine(models.Model):
    name = models.CharField(max_length=100)
    generic_name = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    batch_number = models.IntegerField()

    def __str__(self):
        return self.name