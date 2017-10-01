from django.contrib import admin

from classroom.models import ClassRoom


class ClassRoomAdmin(admin.ModelAdmin):

    list_display = ('name', )


admin.site.register(ClassRoom, ClassRoomAdmin)