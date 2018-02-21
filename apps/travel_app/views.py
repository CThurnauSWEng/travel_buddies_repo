from django.shortcuts import render, HttpResponse, redirect
from .models import Trip
from ..user_app.models import User

def dashboard(request):
    this_user = User.objects.get(id=request.session['user_id'])
    this_users_trips = Trip.objects.filter(travelers=this_user)
    other_trips = Trip.objects.exclude(travelers=this_user)

    context = {
        'this_user'         : this_user,
        'this_users_trips'  : this_users_trips,
        'other_trips'       : other_trips
    }

    return render(request, "travel_app/dashboard.html",context)

def create_trip(request):
    return render(request, "travel_app/add_trip.html")

def process_create_trip(request):
    response = Trip.objects.validate_trip_data(request.POST)

    if (response['status']):
        request.session['errors']  = []
        return redirect('/travels/dashboard')
    else:
        request.session['errors'] = response['errors']
        return render(request, "travel_app/add_trip.html")

    return redirect('/travels/dashboard')

def join_trip(request):
    trip        = Trip.objects.get(id=request.POST['trip_id'])
    this_user   = User.objects.get(id=request.session['user_id'])

    trip.travelers.add(this_user)
    return redirect('/travels/dashboard')

def show_trip(request,trip_id):
    this_trip       = Trip.objects.get(id=trip_id)

    context = {
        'this_trip'      : this_trip,
        'others_on_trip' : User.objects.all().filter(trips=this_trip).exclude(id=request.session['user_id'])
    }
    return render(request, "travel_app/show_trip.html", context)