from django.shortcuts import render
from django.http import HttpResponse
from main.models import *


def index(request):
    
    course=request.GET.get('course')
    year=request.GET.get('year')
    category=request.GET.get('category')
    
    
    
    
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
def faqs(request):
    return render(request, 'faqs.html',{})
def tnc(request):
    return render(request, 'tnc.html',{})
def privacypolicy(request):
    return render(request, 'privacy-policy.html',{})


