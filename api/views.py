from django.shortcuts import render
from django.core.mail import send_mail
from django.shortcuts import redirect
from .forms import ContactForm

def index(request):
    return render(request, 'index.html')

from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponse

def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        # Example of sending an email (customize as needed)
        send_mail(
            subject,
            message,
            email,
            ['abilityassistbest@gmail.com'],
        )
        
    return render(request, 'index.html')


def success_view(request):
    # Your code here
    return render(request, 'index.html')