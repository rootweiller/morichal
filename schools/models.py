from django.db import models
from django.conf import settings
from users.models import Teachers


class Schools(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    address = models.CharField(max_length=150)
    dni = models.CharField(max_length=150)
    codeme = models.CharField(max_length=70, null=True, blank=True)

    def __str__(self):
        return '%s - %s' % (self.name, self.dni)