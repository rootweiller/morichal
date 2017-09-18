from django.contrib import admin

from .models import Teachers, Students


class TeachersAdmin(admin.ModelAdmin):

    list_display = ('document_number', )

admin.site.register(Teachers, TeachersAdmin)


class StudentsAdmin(admin.ModelAdmin):

    list_display = ('document_number', )

admin.site.register(Students, StudentsAdmin)

