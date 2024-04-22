from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    
    return render(request, "alignmentapp/home.html")

def capabilities(request):

    return render(request, "alignmentapp/capabilities.html")

def whyalignment(request):

    return render(request, "alignmentapp/whyalignment.html")

def aboutus(request):

    return render(request, "alignmentapp/aboutus.html")

def contact(request):

    return render(request, "alignmentapp/contact.html")
