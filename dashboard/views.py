from django.shortcuts import render, redirect
from django.contrib import messages
from main import models

def dashboard(request):
    return render(request,'dashboard/index.html')

def create_category(request):
    try:
        if request.method == 'POST':
            print(request.POST)
            name = request.POST['name']
            models.Category.objects.create(name=name)
            messages.success(request,'Successfully created category')
            return redirect('list-category')
    except:
        messages.error(request, ('Error creating category'))
    return render(request,'dashboard/category/create.html')

def list_category(request):
    categories = models.Category.objects.all()
    context = {'categories': categories}
    return render(request,'dashboard/category/list.html', context)

def edit_category(request, id):
    category = models.Category.objects.get(id=id)
    context = {'category': category}
    return render(request,'dashboard/category/edit.html',context)