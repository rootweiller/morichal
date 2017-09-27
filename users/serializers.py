from rest_framework import serializers
from .models import Teachers, Students


class TeachersSerializers(serializers.ModelSerializer):

    class Meta:
        model = Teachers
        fields = '__all__'

    def create(self, validated_data):

        return Teachers.objects.create(**validated_data)


class StundentsSerializers(serializers.ModelSerializer):

    def create(self, validated_data):

        return Students.objects.create(**validated_data)

    class Meta:
        model = Students
        fields = '__all__'

