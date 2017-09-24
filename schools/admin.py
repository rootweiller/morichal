from django.contrib import admin
from .models import Schools


class SchoolsAdmin(admin.ModelAdmin):
    list_display = ('dni', )

admin.site.register(Schools, SchoolsAdmin)