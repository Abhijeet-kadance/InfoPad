from django.contrib.auth.decorators import login_required
from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.db.models import Q
from .models import Room , Topic, Message
from .forms import RoomForm


# Create your views here.

def loginPage(request):
    page = "login"
    
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request , "User Does not Exists !!")

        user = authenticate(request , username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request , "username and password does not exisit !!!")

    context = {"page" : page}

    return render(request ,'base/login_register.html', context)

def registerUser(request):
      
        form = UserCreationForm()

        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                user.username = user.username.lower()
                user.save()
                login(request , user)
                return redirect('home')
            else:
                messages.error(request ,'An error occured during Registrations')

        context={"form" : form}
        return render(request ,'base/login_register.html' , context)

def logoutUser(request):
    logout(request)
    return redirect("home")

def home(request):
    
    
    q = request.GET.get('q') if request.GET.get('q') != None else '' 
    rooms = Room.objects.filter(
        Q(topic__name__icontains=q) |
        Q(name__icontains=q) |
        Q(description__icontains=q)
    )
    room_count = rooms.count()
    topics = Topic.objects.all()
    room_messages = Message.objects.filter(Q(room__topic__name__icontains=q))    
    context = {'rooms' : rooms , 'topics' : topics , "room_count" : room_count,"room_messages":room_messages}
    return render(request , 'base/home.html', context)

def userProfile(request,pk):
    user = User.objects.get(id=pk)
    rooms = user.room_set.all()
    room_messages = user.message_set.all()
    topics = Topic.objects.all()
    context = {'user':user , 'rooms':rooms , 'room_messages':room_messages , 'topics':topics}
    return render(request,'base/profile.html',context)

def room(request , pk):
    room = Room.objects.get(id=pk)
    room_messages = room.message_set.all()
    participants = room.participants.all()
    if request.method == 'POST':
        message = Message.objects.create(
            user=request.user,
            room=room,
            body=request.POST.get('body')
        )
        room.participants.add(request.user)
        return redirect('room', pk=room.id)

    context = {'room' : room , 'room_messages':room_messages , 'participants':participants}
    return render(request , 'base/room.html' , context)

@login_required(login_url="/login")
def deleteMessage(request,pk):
    message = Message.objects.get(id=pk)

    
    if request.user != message.user :
        return HttpResponse('Your are not Allowed to Delete This Message...')
    
    if request.method == 'POST':
        message.delete()
        return redirect('home')
    return render(request,'base/delete.html', {'obj':message})


@login_required(login_url="/login")
def createRoom(request):
    form = RoomForm()
    topics = Topic.objects.all()
    if request.method == 'POST':
        topic_name = request.POST.get('topic')
        topic, created = Topic.objects.get_or_create(name=topic_name)
        form = RoomForm(request.POST)
        # if form.is_valid():
        #     room = form.save(commit=False)
        #     room.host = request.user
        #     room.save()
        Room.objects.create(
            host=request.user,
            topic=topic,
            name=request.POST.get('name'),
            description=request.POST.get('description'),    
        )
        
        return redirect('home')
            
    context = {'form' : form,"topics":topics}
    return render(request , 'base/room_form.html' , context)

@login_required(login_url="/login")
def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    topics = Topic.objects.all()

    if request.user != room.host :
        return HttpResponse('Your are not Allowed to Update This Room...')
    
    if request.method == 'POST':
        topic_name = request.POST.get('topic')
        topic, created = Topic.objects.get_or_create(name=topic_name)
        room.name = request.POST.get('name')
        room.topic = topic
        room.description = request.POST.get('description')
        room.save()
        return redirect('home')
    context = {'form' : form,"topics":topics,"room":room}
    return render(request , 'base/room_form.html' , context)

@login_required(login_url="/login")
def deleteRoom(request,pk):
    room = Room.objects.get(id=pk)

    
    if request.user != room.host :
        return HttpResponse('Your are not Allowed to Delete This Room...')
    
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    return render(request,'base/delete.html', {'obj':room})

