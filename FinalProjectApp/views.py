from django.shortcuts import render
from .forms import BookingForm
from django.core import serializers
from .models import *
from datetime import datetime
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, DestroyAPIView
from rest_framework import viewsets 
from rest_framework import permissions
from django.contrib.auth.models import User
from .serializers import MenuItemSerializer, BookingSerializer, UserSerializer

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def book(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'book.html', context)

def menu(request):
    menu_data = Menu.objects.all()
    main_data = {"menu": menu_data}
    return render(request, 'menu.html', {"menu": main_data})

def reservations(request):
    date = request.GET.get('date', datetime.today().date())
    bookings = Booking.objects.all()
    bookings_json = serializers.serialize('json', bookings)
    data = json.loads(bookings_json)
    pretty_json = json.dumps(data, indent=4)
    return render(request, 'bookings.html', {"bookings":pretty_json})

def display_menu_item(request, pk=None): 
    if pk: 
        menu_item = Menu.objects.get(pk=pk) 
    else: 
        menu_item = "" 
    return render(request, 'menu_item.html', {"menu_item": menu_item}) 

@csrf_exempt
def bookings(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        exist = Booking.objects.filter(reservation_date=data['reservation_date']).filter(reservation_slot=data['reservation_slot']).exists()
        if exist == False:
            booking = Booking(
                first_name=data['first_name'],
                reservation_date=data['reservation_date'],
                reservation_slot=data['reservation_slot'],
            )
            booking.save()
        else:
            return HttpResponse(json.dumps({'error':1}), content_type='application/json')
        
    date = request.GET.get('date', datetime.today().date())
    bookings = Booking.objects.filter(reservation_date=date)
    booking_json = serializers.serialize('json', bookings)

    return HttpResponse(booking_json, content_type='application/json')

class MenuItemsView(ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class SingleMenuItemView(RetrieveUpdateAPIView, DestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


