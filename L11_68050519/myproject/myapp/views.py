from django.shortcuts import render, redirect  # เพิ่ม redirect ตรงนี้
from django.http import HttpResponse
from .models import Person 

def index(request):
    persons = Person.objects.all() 
    return render(request, "index.html", {'persons': persons})

def about(request):
    return HttpResponse("<h1>เกี่ยวกับเรา</h1>")

def form(request):
    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")
      
        Person.objects.create(
            name=name,
            age=age
        )
    
        return redirect("/")
        
    else:
        return render(request, 'form.html') 

def contact(request):
    return HttpResponse("<h1>68053881 ณัฐพล วงค์ชมภู</h1>")