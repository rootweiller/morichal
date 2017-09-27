from django.shortcuts import render

from rest_framework import viewsets
from .serializers import TeachersSerializers, StundentsSerializers
from .models import Teachers, Students


class Teachers(viewsets.ModelViewSet):

    serializer_class = TeachersSerializers

    model = Teachers

    queryset = model.objects.all()

    def filter_queryset(self, queryset):

        return self.queryset

    def filter_queryset(self, queryset):

        query = {}

        if self.request.GET.get('document_number'):
            query['document_number'] = self.request.GET.get('document_number')
        if self.request.GET.get('document_type'):
            query['docuemnt_type'] = self.request.GET.get('document_type')

        return self.model.objects.filter(**query)

        return self.queryset


class Students(viewsets.ModelViewSet):

    serializer_class = StundentsSerializers
    model = Students
    queryset = model.objects.all()

    def filter_queryset(self, queryset):

        query = {}

        if self.request.GET.get('document_number'):
            query['document_number'] = self.request.GET.get('document_number')
        if self.request.GET.get('document_type'):
            query['docuemnt_type'] = self.request.GET.get('document_type')

        return self.model.objects.filter(**query)

        return self.queryset