from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Items
from .forms import ItemForm

# Create your views here.
def index(request):
    data = Items.objects.all()
    
    context = {
        "Item_list" : data
    }
    return render(request, "myapp/index.html", context)

def details(request,id):
    item = Items.objects.get(id = id)
    context = {
        "item" : item
    }
    return render(request,'myapp/details.html', context )

def friends(request):
    friends_list = ['Mohan', 'Chirag', 'Pranav', 'Abhishek']
    return HttpResponse("<h1>" + friends_list[3] + "</h1>")
    
def create_item(request):
    form = ItemForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('myapp:index')
        
    context = {
        'form' : form
    }
    return render(request, 'myapp/item-form.html', context)