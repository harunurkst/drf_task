# Django
from django.db import models


class Contact(models.Model):
    """
    Model for each contact entry
    """
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=50)

    def __str__(self):
        return str(self.name)
