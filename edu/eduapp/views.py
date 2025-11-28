from django.shortcuts import render

def homepage(request):
    return render(request, 'homepage.html')



def about(request):
    return render(request, 'aboutpage.html')

def contact(request):
    return render(request, 'contactpage.html')

def courses(request):
    return render(request, 'coursespage.html')

def blog(request):
    return render(request, 'blogpage.html')