from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, "index.html")
def about(request):
    return render(request, "about.html")
def form(request):
    return render(request, "form.html")

def contact(request):
    return HttpResponse("<h1>69053881 ณัฐพล วงค์ชมภู</h1>")