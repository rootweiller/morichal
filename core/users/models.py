from __future__ import unicode_literals

from django.db import models
from django.core.mail import send_mail
#from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _

from .managers import UserManager


class User(AbstractBaseUser):
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    is_active = models.BooleanField(_('active'), default=True)
    is_staff = models.BooleanField(default=False)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        '''
        Returns the first_name plus the last_name, with a space in between.
        '''
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        '''
        Returns the short name for the user.
        '''
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        '''
        Sends an email to this User.
        '''
        send_mail(subject, message, from_email, [self.email], **kwargs)


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


class Teachers(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=30)
    education = models.ForeignKey(Education)
    document_type = models.CharField(max_length=4, choices=DOCUMENT_TYPE)
    document_number = models.CharField(max_length=15)
    university = models.CharField(max_length=30)

    def __str__(self):
        return '%s - %s' % (self.document_type, self.document_number)


class Students(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=80)
    education = models.CharField(max_length=90)
    age = models.DateField()
    document_type = models.CharField(max_length=4, choices=DOCUMENT_TYPE)
    document_number = models.CharField(max_length=15)

    def __str__(self):
        return self.document_number
