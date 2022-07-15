from django.http import HttpResponse
from django.shortcuts import render
from polls.forms import BMIForm
from polls.forms import SearchForm
from django.urls import reverse
from polls.forms import NewProfile
from .models import Profile
from django.db.models import Q 

def bmi_intro(request):
    if request.method == "POST":
        form = BMIForm(request.POST)
        if form.is_valid():
            height = request.POST.get('height')
            weight = request.POST.get('weight')
            height = float(height)
            weight = float(weight)
            result = weight/(height * height)
            return HttpResponse(f'<h1>Your BMI is {result}</h1>')
    else:
        form = BMIForm()
    return render(request, 'polls/bmi.html', {'form': form})
    
def search_profiles(request):
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            search = request.POST.get('search')
            queryset = Profile.objects.filter(Q(name__icontains = search | Q(relation__icontains = search))
            return render (request, 'polls/search_results.html', {'profiles' : queryset})
    else:
        form = SearchForm()
    return render(request, 'polls/search.html', {'form': form})

def newprofile(request):
    if request.method == "POST":
        form = NewProfile(request.POST)
        if form.is_valid():
            p = Profile(name=form.cleaned_data['name'], 
                age=form.cleaned_data['age'],
                address=form.cleaned_data['address'],
                gender=form.cleaned_data['gender'],
                phone_number=form.cleaned_data['phone_number'],
                occupation=form.cleaned_data['occupation'],
                relation=form.cleaned_data['relation'],
                extra=form.cleaned_data['extra'])
            p.save()
            return HttpResponse('New profile has been saved!')
    else:
        form = NewProfile()
    return render(request, 'polls/newprofile.html', {'form': form})

def home(request):
    if request.method == "POST":
        if 'search' in request.POST:
            form = SearchForm()
            return render(request, 'polls/search.html', {'form': form})
        elif 'newprofile' in request.POST:
            form = NewProfile()
            return render(request, 'polls/newprofile.html', {'form': form})
        elif 'display' in request.POST:
            data = Profile.objects.all()
            return render(request, 'polls/display.html', {'profiles': data})
            
    else: 
        return render(request, 'polls/home.html')
    
def display(request):
    if request.method == "POST":
        data = Profile.objects.all()
        return render(request, "polls/display.html", {'profiles': data})
    else:
        data = Profile.objects.all()
        return render(request, "polls/display.html", {'profiles': data})
        

