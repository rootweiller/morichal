from rest_framework import serializers

from classroom.models import ClassRoom


class ClassRoomSerializers(serializers.ModelSerializer):

    def create(self, validated_data):

        return ClassRoom.objects.create(**validated_data)

    class Meta:
        model = ClassRoom
        fields = '__all__'