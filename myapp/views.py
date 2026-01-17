from django.shortcuts import render
from django.http import HttpResponse
from .models import Items

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
    



