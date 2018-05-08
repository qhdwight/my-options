from django.shortcuts import render
from django.shortcuts import redirect

def root(request):
    return redirect('home')

def home(request):
    return render(request, 'home.html')

def program_finder(request):
    return render(request, 'program_finder.html')

def about(request):
    return render(request, 'about.html')