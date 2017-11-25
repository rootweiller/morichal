from django.db import models
from django.conf import settings
from users.models import Teachers, Students


class Schools(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    address = models.CharField(max_length=150)
    dni = models.CharField(max_length=150)
    codeme = models.CharField(max_length=70, null=True, blank=True)

    def __str__(self):
        return '%s - %s' % (self.name, self.dni)


class ClassRoom(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    teacher = models.ForeignKey(Teachers)
    schools = models.ForeignKey(Schools)
    students = models.ForeignKey(Students)

    def __str__(self):
        return self.name


class SchoolsSubjects(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    schools = models.ForeignKey(Schools)

    def __str__(self):
        return '%s - %s' % (self.name, self.schools)


class SchoolsGrades(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    calification = models.IntegerField()
    subjects = models.ForeignKey(SchoolsSubjects)

    def __str__(self):

        return str(self.calification)