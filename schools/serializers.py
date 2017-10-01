from rest_framework import serializers
from .models import Schools


class SchoolsSerializers(serializers.ModelSerializer):

    def create(self, validated_data):

        return Schools.objects.create(**validated_data)

    class Meta:

        model = Schools
        fields = '__all__'





