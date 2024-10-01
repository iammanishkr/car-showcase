from django.shortcuts import render, redirect
from .models import Car
from .forms import CarForm

# Create your views here.

def add_car(request):
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES) 
        if form.is_valid():  
            form.save()
            return redirect('index')
    else:
        form = CarForm()
    return render(request, 'add_car.html', {'form': form})

def index(request):
    cars = Car.objects.all() 
    return render(request, 'index.html', {'cars': cars})
