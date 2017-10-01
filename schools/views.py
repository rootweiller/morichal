from django.shortcuts import render
from rest_framework import viewsets
from .serializers import SchoolsSerializers
from .models import Schools


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


