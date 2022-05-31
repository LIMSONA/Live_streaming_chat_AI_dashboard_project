from django.shortcuts import render

# Create your views here.

def home(requests):
    return render(requests, 'gf_kafka/gf_kafka.html')
