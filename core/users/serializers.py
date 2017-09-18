from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Teachers, Students


class DocumentNumber(object):
    def __init__(self, queryset, message=None):
        self.base = UniqueValidator(queryset, message)


class TeachersSerializers(serializers.Serializer):
    document_number = serializers.CharField(
        validators=[DocumentNumber(Teachers.objects.all())])

    class Meta:
        fields = ('phone', 'document_number', 'document_type', 'education',
                  'university')

    def create(self, validated_data):

        return Teachers.objects.create(**validated_data)


class StundentsSerializers(serializers.Serializer):
    document_number = serializers.CharField(
        validators=[DocumentNumber(Students.objects.all)])

    class Meta:
        fields = ('phone', 'document_number', 'document_type', 'age',
                  'education')

    def create(self, validated_data):

        return Students.objects.create(**validated_data)