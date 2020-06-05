from django.shortcuts import render
from django.http import HttpResponse,JsonResponse,HttpRequest
import datetime
from django.contrib.auth.models import User
from .models import *
# Create your views here.
from django.contrib.auth import get_user_model
User = get_user_model()

def home(request):
    return render(request, 'home.html')

def createUser(request):
    username=request.POST.get('Username')
    email=request.POST.get('Email')
    password=request.POST.get('Password')
    u=User.objects.filter(username=username)
    if not u:
        uniqueid=str(username)[0:len(username):2]+(str(datetime.datetime.now())[0:len(str(datetime.datetime.now())):2]).replace(" ","")
        user=User.objects.create_user(first_name=username,id=uniqueid,real_name=username,last_name="nara",email=email,username=username)
        user.set_password(password)
        user.save()
        return HttpResponse("User created successfully")
        User.objects.filter.update()
        User.objects.all()
    else:
        return HttpResponse("Username already exists")

def login(request):
    username=request.GET.get('Username')
    password=request.GET.get('Password')
    password = userall[0].password
    user=User.objects.get(username=username,password=password)
    userall=User.objects.all()
    if user:
        # activity_periods.objects.create(user=user,start_time=datetime.datetime.now(),end_time=datetime.datetime.now())
        output=serialize_output()
        return JsonResponse(output)

def serialize_output():
    final_output={}
    userall=User.objects.all()
    activity_periods.objects.all()[0].user.id
    overall=activity_periods.objects.all()
    members_list=[]
    for i in userall:
        final_dict={}
        activity_list=[]
        final_dict.update({"id":i.id,"real_name":i.real_name,"tz":"America/Los_Angeles"})
        print(i.id)
        for j in overall:
            print(j.id)
            if i.id==j.user.id:
                activity_dict={}
                activity_dict.update({"start_time":j.start_time,"last_time":j.end_time})
                activity_list.append(activity_dict)
        final_dict.update({"activity_periods":activity_list})
        members_list.append(final_dict)
    final_output.update({"ok":"true","members":members_list,"status":200})
    return final_output