from rest_framework import serializers
from .models import *
from django.contrib.auth import get_user_model;


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserData
        fields = ["id", "email", "name", "password"]

    def create(self, validated_data):
        user = UserData.objects.create(email=validated_data['email'],
                                       name=validated_data['name']
                                         )
        user.set_password(validated_data['password'])
        user.save()
        return user
    
class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model=Booking
        fields=('id','name','date')

class AssociationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Association
        fields=('adress', 'coordinateX', 'coordinatY')

class BookedTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model=BookedTime
        fields=('timeslot','booking_object','booked_by','date')