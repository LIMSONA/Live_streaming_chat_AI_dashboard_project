from django.shortcuts import render

# Create your views here.

def home(requests):
    return render(requests, 'gf_spark/gf_spark.html')
