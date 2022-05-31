from django.shortcuts import render

# Create your views here.

def home(requests):
    return render(requests, 'dj_dash/dj_dash.html')
