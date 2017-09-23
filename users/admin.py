from django.contrib import admin

from .models import Teachers, Students, Education, User


class UserAdmin(admin.ModelAdmin):
    list_display = ('email', )

admin.site.register(User, UserAdmin)


class TeachersAdmin(admin.ModelAdmin):

    list_display = ('document_number', )

admin.site.register(Teachers, TeachersAdmin)


class StudentsAdmin(admin.ModelAdmin):

    list_display = ('document_number', )

admin.site.register(Students, StudentsAdmin)


class EducationAdmin(admin.ModelAdmin):

    list_display = ('name', )

admin.site.register(Education, EducationAdmin)