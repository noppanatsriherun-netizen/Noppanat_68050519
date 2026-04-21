from django.shortcuts import render, redirect, get_object_or_404  # เพิ่ม get_object_or_404 ตรงนี้
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


def edit(request, person_id):
    person = get_object_or_404(Person, pk=person_id)
    
    if request.method == "POST":

        name = request.POST.get("name")
        age = request.POST.get("age")
        person.name = name
        person.age = age
        person.save()
        return redirect("/")
    else:
        # แสดงฟอร์มแก้ไข
        return render(request, "edit.html", {"person": person})
def delete(request, person_id):
    person = get_object_or_404(Person, pk=person_id)
    person.delete()
    return redirect("/")