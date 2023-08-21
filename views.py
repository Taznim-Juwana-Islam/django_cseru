from django.http import HttpResponse
from django.shortcuts import render
def homePage(request):
    return render(request,"index.html")

def aboutUs(request):
    return HttpResponse("<b>welcome this is Taznim Juwana</b>")
