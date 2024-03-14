from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import ContactMessage
# Create your views here.

def home(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        ContactMessage.objects.create(name=name, email=email, subject=subject, message=message)
        return HttpResponseRedirect('/thank-you/')
    
    return render(request, 'index.html')


# def contact(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         subject = request.POST.get('subject')
#         message = request.POST.get('message')
#         ContactMessage.objects.create(name=name, email=email, subject=subject, message=message)
#         return HttpResponseRedirect('/thank-you/')
#     return render(request, 'contactform/contact.html')