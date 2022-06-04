from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html',{})


def account(request):
    return render(request, 'account.html',{})

def assignments(request):
    return render(request, 'assignments.html',{})

def certificate(request):
    return render(request, 'certificate.html',{})

def contacts(request):
    return render(request, 'contacts.html',{})

def degree(request):
    return render(request, 'degree.html',{})

def diploma(request):
    return render(request, 'diploma.html',{})

def events(request):
    return render(request, 'events.html',{})

def examnotes(request):
    return render(request, 'examnotes.html',{})

def exams(request):
    return render(request, 'exams.html',{})

def pgprogram(request):
    return render(request, 'pgprogram.html',{})

def profile(request):
    return render(request, 'profile.html',{})

def questionpaper(request):
    return render(request, 'questionpaper.html',{})

def search(request):
    return render(request, 'search.html',{})

def worpro(request):
    return render(request, 'worpro.html',{})
