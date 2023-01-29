from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Room
from .models import Booking
from .forms import BookingForm
# Create your views here.


def home(requset):
    return render(requset, 'cat_hotel/home.html')


def about(requset):
    return render(requset, 'cat_hotel/about.html')


def profile(requset):
    return render(requset, 'cat_hotel/profile.html')



def cat_hotels(requset):
    all_rooms = Room.objects.all()
    context = {'cat_hotels': all_rooms}
    return render(requset,'cat_hotel/cat_hotels.html', context)


def cat_hotel(request, number_room):
    one_room = Room.objects.get(number_room=number_room)
    if request.method == 'POST':
        start_date = request.POST.get('start_date')
        start_time = request.POST.get('start_time')
        end_date = request.POST.get('end_date')
        end_time = request.POST.get('end_time')
        cat = request.POST.get('cat')
        phone_number = request.POST.get('phone_number')

        obj, created = CatHotel.objects.get_or_create(
            room=one_room,
            start_date=start_date,
            start_time=start_time,
            end_date=end_date,
            end_time=end_time,
            cat=cat,
            phone_number=phone_number
        )
        obj.save()
        return redirect('success')
    context = {'cat_hotel': one_room}
    return render(request, 'cat_hotel/cat_hotel.html', context)
    


def success(request):
    return render(request, 'success.html')


def completed(requset):
    return render(requset,'cat_hotel/completed.html')

def edit_completed(requset):
    return render(requset,'cat_hotel/edit_completed.html')