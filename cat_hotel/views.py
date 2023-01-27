from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Room
from .models import Booking
from .froms import BookingForm
# Create your views here.


def home(requset):
    return render(requset, 'cat_hotel/home.html')


def about(requset):
    return render(requset, 'cat_hotel/about.html')


def profile(requset):
    return render(requset, 'cat_hotel/profile.html')


def login_user(requset):
    return render(requset, 'cat_hotel/login_user.html')


def cat_hotels(requset):
    all_rooms = Room.objects.all()
    context = {'cat_hotels': all_rooms}
    return render(requset,'cat_hotel/cat_hotels.html', context)

def cat_hotel(request, number_room):
    one_room = None
    try:
        one_room = Room.objects.get(number_room=number_room)
        url = reverse('cat_hotel', args=[number_room])
    except Room.DoesNotExist:
        print('Room not found')

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = BookingForm()
        
    context = { 'cat_hotel': one_room, 'form': form }
    return render(request, 'cat_hotel/cat_hotel.html', context)


def success(request):
    return render(request, 'success.html')


def completed(requset):
    return render(requset,'cat_hotel/completed.html')

def edit_completed(requset):
    return render(requset,'cat_hotel/edit_completed.html')