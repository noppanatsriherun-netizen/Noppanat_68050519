from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.db.models import Q  # เพิ่ม import Q ตรงนี้
from .models import Person 

def index(request):
    # 1. ดึงข้อมูลประชากรทั้งหมดมาก่อน (กรณีที่ยังไม่ได้ค้นหา)
    persons = Person.objects.all() 
    
    # 2. รับค่าคำค้นหาจากช่องค้นหา (name="q")
    query = request.GET.get('q')
    
    # 3. ตรวจสอบว่ามีค่าค้นหาถูกพิมพ์ส่งมาหรือไม่
    if query:
        # 4. ถ้ามีคำค้นหา ให้กรองข้อมูลเฉพาะคนที่ชื่อ (name) หรือ อายุ (age) ตรงกับคำค้นหา
        # (หมายเหตุ: ใน PDF พิมพ์ age_icontains ตก _ ไปหนึ่งตัว ที่ถูกต้องคือ age__icontains)
        persons = persons.filter(Q(name__icontains=query) | Q(age__icontains=query))
        
    # ส่งข้อมูลไปแสดงผลที่ template
    return render(request, "index.html", {'persons': persons})

# ... ฟังก์ชันอื่นๆ (about, form, contact, edit, delete) ยังคงเหมือนเดิม ...
def about(request):
    return HttpResponse("<h1>เกี่ยวกับเรา</h1>")

def form(request):
    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")
      
        Person.objects.create(name=name, age=age)
        return redirect("/")
    else:
        return render(request, 'form.html') 

def contact(request):
    return HttpResponse("<h1>68053881 ณัฐพล วงค์ชมภู</h1>")

def edit(request, person_id):
    person = get_object_or_404(Person, pk=person_id)
    if request.method == "POST":
        person.name = request.POST.get("name")
        person.age = request.POST.get("age")
        person.save()
        return redirect("/")
    else:
        return render(request, "edit.html", {"person": person})

def delete(request, person_id):
    person = get_object_or_404(Person, pk=person_id)
    person.delete()
    return redirect("/")