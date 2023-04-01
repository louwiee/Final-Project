from django.shortcuts import render
from .models import Movie, Rental, DetailRental
from .forms import RentalForm
from .models import Membership
from django.shortcuts import render, redirect, get_object_or_404



# Create your views here.

from django.http import HttpResponse

def home(request):

    Movies = Movie.objects.all()

    return render(request, 'rent.html', {'Movies':Movies})


def addrent(request,pk):

    form = RentalForm()

    if request.method == 'POST':

        form = RentalForm(request.POST)

        if form.is_valid():
            form.save()

    return render(request, 'addrent.html', {'form':form})

def profile_page(request,pk):
    
    #get user's car rents
    user = request.user
    profile = Membership.objects.get(user=user)
    

    return render(request, 'member.html', {'profile':profile})




