from django.shortcuts import render
from .models import checking
from .models import certificates

from django.http import HttpResponse


def index(request):
   # return HttpResponse("messege from home ") 
    hold = checking.objects.all()
    holder = {'hold':hold}
    return render(request, "index.html", holder)

def Certificates(request):
   certificates_doc=certificates.objects.all()
 
   return render(request, "certificates.html", {'certficates_doc':certificates_doc})
   



    