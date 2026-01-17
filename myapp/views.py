from django.shortcuts import render
from django.http import HttpResponse
from .models import Items

# Create your views here.
def index(request):
    data = Items.objects.all()
    return render(request, "myapp/index.html")

                  
def friends(request):
    friends_list = ['Mohan', 'Chirag', 'Pranav', 'Abhishek']
    return HttpResponse("<h1>" + friends_list[3] + "</h1>")
    



