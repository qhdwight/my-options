from django.shortcuts import render
from django.shortcuts import redirect

from programfinder.forms import FindScholarshipForm
from programfinder.models import Scholarship

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
    template_data = {'currentNav': 'program-finder'}
    if request.method == 'POST':
        search_form = FindScholarshipForm(request.POST)
        if search_form.is_valid():
            search_query = Scholarship.objects.all()
            if search_form.cleaned_data['lower_amount']:
                search_query.filter(amount__gte=search_form.cleaned_data['lower_amount'])
            if search_form.cleaned_data['upper_amount']:
                search_query.filter(amount__lte=search_form.cleaned_data['upper_amount'])
            if search_form.cleaned_data['deadline_month']:
                search_query.filter(deadlineDay=search_form.cleaned_data['deadline_month'])
            template_data['searchForm'] = search_form
            template_data['searchResults'] = search_query
            return render(request, 'scholarship_finder.html', template_data)
    search_form = FindScholarshipForm()
    template_data['searchForm'] = search_form
    return render(request, 'scholarship_finder.html', template_data)
    