from django.shortcuts import render
from.models import Departmet
from.models import doctor
from.forms import BookingForm
from.forms import ContactForm


# Create your views here.
def index(request):
    dict_dept={
        'dept':Departmet.objects.all()
    }
    return render(request,'index.html',dict_dept)
def about(request):
    return render(request,'about.html')
def booking(request):
    if request.method =="POST":
        form=BookingForm(request.POST)
        if form.is_valid():
            pass
            form.save()  
            return render(request,'ok.html') 
    form=BookingForm()
    dict_form={
        'form':form
    }
    return render(request, 'booking.html', dict_form)
def contact(request):
    if request.method=="POST":
        contact_form=ContactForm(request.POST)
        if contact_form.is_valid():
            pass
            contact_form.save()
            return render(request,'send.html') 
    contact_form=ContactForm()
    dict_con_form={
        'contact_form':contact_form
    }
    return render(request,'contact.html',dict_con_form)
def doctors(request):
    dict_doctor={
        'doc':doctor.objects.all()
    }

    return render(request,'doctors.html',dict_doctor)
def department(request):
    dict_dept={
        'dept':Departmet.objects.all()
    }
    return render(request,'department.html',dict_dept)