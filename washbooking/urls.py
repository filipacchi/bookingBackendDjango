from django.urls import path
from . import views
from django.conf import settings
from rest_framework.authtoken.views import obtain_auth_token
from .views import *
from django.urls import re_path

urlpatterns = [
    path('delete/<int:pk>/', views.deleteBooking),
    path('auth/register/',
        RegisterView.as_view(),
        name='auth_user_create'),
    path('book/get/', GetBookingsAPIVIEW.as_view(), name='get_all_bookings'),
    path('book/user/', GetUserBookingAPIVIEW.as_view(), name='get_user_bookings'),
    path('book/add/', CreateBookingAPIVIEW.as_view(), name='add_booking'),
    path('book/get/object/<int:object_pk>', GetBookingsFromObject.as_view(), name='get_booking_object'),
    path('validate', checkValidationAPIVIEW.as_view(), name='check_validation'),
    path('getA', GetUsersAssociationsAPIVIEW.as_view(), name="GetUsersAssociationsAPIVIEW")
]