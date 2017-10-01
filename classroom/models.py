from django.db import models
from morichal import settings
from schools.models import Schools
from users.models import Teachers


class ClassRoom(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    teacher = models.ForeignKey(Teachers)
    schools = models.ForeignKey(Schools)

    def __str__(self):
        return self.name


class Score(models.Model):
    score = models.IntegerField()
    student = models.ForeignKey(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)

    def __str__(self):
        return self.score