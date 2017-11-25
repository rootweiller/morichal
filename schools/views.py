from django.shortcuts import render
from rest_framework import viewsets
from .serializers import SchoolsSerializers, ClassRoomSerializers
from .models import Schools, ClassRoom


class Schools(viewsets.ModelViewSet):
    serializer_class = SchoolsSerializers
    model = Schools
    queryset = model.objects.all()

    def filter_queryset(self, queryset):

        query = {}

        if self.request.GET.get('dni'):
            query['dni'] = self.request.GET.get('dni')
        if self.request.GET.get('name'):
            query['name'] = self.request.GET.get('name')
        return self.model.objects.filter(**query)


class ClassRoom(viewsets.ModelViewSet):

    serializer_class = ClassRoomSerializers
    model = ClassRoom
    queryset = model.objects.all()

    def filter_queryset(self, queryset):

        query = {}

        if self.request.GET.get('teacher'):
            query['teacher__name'] = self.request.GET.get('teacher')
        if self.request.GET.get('name'):
            query['name'] = self.request.GET.get('name')

        return self.model.objects.filter(**query)