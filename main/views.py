from django.shortcuts import render

def home(request):
    return render(request,'front/index.html')

def about(request):
    return render(request,'front/about.html')

def contact(request):
    return render(request,'front/contact.html')

def news(request):
    return render(request,'front/news.html')