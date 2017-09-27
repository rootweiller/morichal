from rest_framework import serializers
from .models import ClassRoom, Schools


class SchoolsSerializers(serializers.ModelSerializer):

    def create(self, validated_data):

        return Schools.objects.create(**validated_data)

    class Meta:

        model = Schools
        fields = '__all__'


class ClassRoomSerializers(serializers.ModelSerializer):

    def create(self, validated_data):

        return ClassRoom.objects.create(**validated_data)

    class Meta:
        model = ClassRoom
        fields = '__all__'


