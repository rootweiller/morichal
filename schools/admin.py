from django.contrib import admin
from .models import Schools, SchoolsGrades, ClassRoom


class ClassRoomAdmin(admin.ModelAdmin):

    list_display = ('name', 'user' )


class SchoolsAdmin(admin.ModelAdmin):
    list_display = ('dni', 'user', )


class SchoolsGradesAdmin(admin.ModelAdmin):
    list_display = ('calification', )


admin.site.register(Schools, SchoolsAdmin)
admin.site.register(SchoolsGrades, SchoolsGradesAdmin)
admin.site.register(ClassRoom, ClassRoomAdmin)