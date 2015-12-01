from django.db import models


# Create your models here.

class Comment(models.Model):
    name = models.CharField(max_length=20)
    phone = models.CharField(max_length=11)
    body = models.CharField(max_length=2000, blank=True)

    def __str__(self):
        return self.body[:100]
