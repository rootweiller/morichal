from rest_framework import serializers
from .models import Teachers, Students, User


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


class UserSerializers(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):

        user = User(username=validated_data['username'],
                    first_name=validated_data['first_name'],
                    last_name=validated_data['last_name'],
                    email=validated_data['email'],
                    document_number=validated_data['document_number'])
        user.set_password(validated_data['password'])
        user.save()