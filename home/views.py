from django.shortcuts import render,redirect,HttpResponse
from datetime import datetime
from django.contrib import messages
from home.models import Contact
from django.contrib import messages



# Create your views here.
def index(request):
    messages.success(request,"This is an icecream site")
    return render(request,"base.html")

def about(request):
    return render(request,"about.html")

def services(request):
    return render(request,"services.html")

def contact(request):
    if request.method == 'POST':
        # Process the form data
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        contact = Contact(name = name , email = email ,phone = phone , date = datetime.today())
        contact.save()
        messages.success(request, "Your message has been sent! ")

    return render(request,"contact.html")
