from django.shortcuts import render
from django.shortcuts import redirect

def root(request):
    return redirect('home')

def home(request):
    return render(request, 'home.html', {'currentNav' : 'home'})

def program_finder(request):
    return render(request, 'program_finder.html', {'currentNav' : 'program-finder'})

def resources(request):
    return render(request, 'resources.html', {'currentNav' : 'resources'})

def about(request):
    return render(request, 'about.html', {'currentNav' : 'about'})

def scholarship_finder(request):
    return render(request, 'scholarship_finder.html', {'currentNav' : 'program-finder'})