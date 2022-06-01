from django.shortcuts import render
from django.http.response import StreamingHttpResponse
import requests


# Create your views here.

def home(requests):
    return render(requests, 'home/home.html')


