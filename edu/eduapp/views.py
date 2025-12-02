from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

def homepage(request):
    return render(request, 'homepage.html')



def about(request):
    return render(request, 'aboutpage.html')



def courses(request):
    return render(request, 'coursespage.html')

def blog(request):
    return render(request, 'blogpage.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        full_message = f"Message from {name} ({email}):\n\n{message}"

        send_mail(
            subject,
            full_message,
            "KatCompany <kwabby950@gmail.com>",  # Use verified sender
            ["kwabby950@gmail.com"],  # Your receiving email
            fail_silently=False,
        )

        return render(request, 'contactpage.html', {"success": True})

    return render(request, 'contactpage.html')
