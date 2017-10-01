from django.db import models

DOCUMENT_TYPE = (
    ('CI', 'CEDULA DE IDENTIDAD'),
    ('PA', 'PASAPORTE'),
    ('DNI', 'DOCUMENTO DE IDENTIDAD')
)


class Education(models.Model):
    name = models.CharField(max_length=80)
    description = models.CharField(max_length=80)

    def __str__(self):
        return self.name