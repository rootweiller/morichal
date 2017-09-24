from django.contrib import admin
from .models import Schools, ClassRoom


class SchoolsAdmin(admin.ModelAdmin):
    list_display = ('dni', )

admin.site.register(Schools, SchoolsAdmin)


class ClassRoomAdmin(admin.ModelAdmin):

    list_display = ('name', )


admin.site.register(ClassRoom, ClassRoomAdmin)