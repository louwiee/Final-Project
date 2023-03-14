from django.shortcuts import render
from .models import Movie
from .forms import RentalForm

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



