from django import forms

from users.models import Students


class StudentsAddForm(forms.Form):

    class Meta:

        model = Students