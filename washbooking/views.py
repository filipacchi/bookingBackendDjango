from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from .serializer import BookingSerializer
from django.http import Http404
from rest_framework import status
from django.contrib.auth import get_user_model
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import *
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from .serializer import *
from django.contrib.auth.mixins import PermissionRequiredMixin
from .permissions import *

@api_view(['GET'])
def getBooking(request):
    booking = Booking.objects.all()
    serializer = BookingSerializer(booking, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def postBooking(request):
    serializer = BookingSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
@api_view(['DELETE'])
def deleteBooking(request, pk):
    try:
        booking = Booking.objects.get(pk=pk)
        booking.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Booking.DoesNotExist:
            raise Http404

class RegisterView(APIView):
    authentication_classes = []
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


#####
#Inte min egna kod, ett exempel som vi kan jobba utifrån
# class CreateUserAPIView(CreateAPIView):
#     serializer_class = CreateUserSerializer
#     permission_classes = [AllowAny]

#     def create(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         self.perform_create(serializer)
#         headers = self.get_success_headers(serializer.data)
#         # We create a token than will be used for future auth
#         token = Token.objects.create(user=serializer.instance)
#         token_data = {"token": token.key}
#         return Response(
#             {**serializer.data, **token_data},
#             status=status.HTTP_201_CREATED,
#             headers=headers
#         )


class LogoutUserAPIView(APIView):
    queryset = get_user_model().objects.all()

    def get(self, request, format=None):
        # simply delete the token to force a login
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)
    #####

class GetUserBookingAPIVIEW(APIView):
    permission_classes = [IsAuthenticated]#[checkGroup]
    def get(self, request):
        user = self.request.user
        person = Person.objects.get(user=user.id)
        user_associations = person.associations.all()
        print(user_associations)
        for association in user_associations:
            bookable_object = BookableObject.objects.filter(inAssociation=association)
            for object in bookable_object:
                print(BookedTime.objects.filter(booking_object=object))
        return Response("GetUserBooking")
    
class GetBookingsAPIVIEW(APIView):
    permission_classes= [AllowAny]#[checkGroup]
    def get(self,request):
        print(self.request.data)
        bookings = BookedTime.objects.all()
        serializer = BookedTimeSerializer(bookings, many=True)
        return Response(serializer.data)
    
class GetBookingsFromObject(APIView):
    permission_classes=[IsAuthenticated]
    def get(self,request,object_pk):
        bookable_object = BookableObject.objects.get(objectId=object_pk)
        bookings = BookedTime.objects.filter(booking_object=bookable_object)
        serializer = BookedTimeSerializer(bookings, many=True)
        print(bookings)
        return Response(serializer.data)
    
class CreateBookingAPIVIEW( APIView):
    permission_classes= []
    def post(self,request):
        serializer = BookedTimeSerializer(data=request.data)
        if serializer.is_valid():
            print("Sparar")
            serializer.save()
            return Response(serializer.data)
        else: print("NOT VALID")
        return Response("An error occured, this time might not be available")

class checkValidationAPIVIEW(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        return Response("Validated")
    
class GetUsersAssociationsAPIVIEW(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        user = self.request.user
        person = Person.objects.get(user=user.id)
        user_associations = person.associations.all()
        print(user_associations)
        return Response("Asso")