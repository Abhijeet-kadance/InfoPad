from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
rooms = [
    {'id':1, 'name':'Lets Learn Python'},
    {'id':2, 'name':'Lets Learn JavaScript'},
    {'id':3, 'name':'Lets Learn Go Language'},
]
def home(request):
    context = {'rooms':rooms}
    return render(request, 'base/home.html',context)


def room(request):
    return render(request,'base/room.html',{'rooms':rooms})