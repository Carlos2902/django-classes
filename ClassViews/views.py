from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views import View
from datetime import datetime

class HomeView(View):
    def get(self, request):
        return HttpResponse('Wlelcome')

class AboutView(View):
    def get(self, request):
        return HttpResponse('About')
    

def displayYear(request):
    todaysYear = datetime.today().year
    return HttpResponse(todaysYear)