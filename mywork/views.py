from django.shortcuts import render
from django.http import HttpResponse
def work(request):
    return HttpResponse("messege from mywork ")

def home(request):
    return HttpResponse("messege from home ") 