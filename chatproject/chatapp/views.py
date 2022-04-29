from django.shortcuts import render
from django.http import HttpResponse
from .models import user

from pymongo import MongoClient
# Create your views here.
connection = MongoClient('localhost',27017)
db_rakesh = connection['rakesh']
collection_users = db_rakesh['users']

def login(request):
    if request.session.get('username'):
        return render(request,'chat_homepage.html',{"user":request.session.get('username')})
    return render(request,'login.html')

def login_validation(request):
    username = request.GET.get("username")
    password = request.GET.get("password")
    print(username)
    if username == None or username =="":
        return render(request,'login.html',{"msg":"please enter the credentials"})
    doc = collection_users.find({"username":username})
    data = doc.next()
    print(data["username"])
    if data["username"]==username and data["password"]==password:
        request.session['username'] = username
        return render(request,'chat_homepage.html',{"user":request.session.get('username')})
    else:
        return render(request,'login.html',{"msg":"invalid user credentials"})


def chat_homepage(request):
    return render(request,'chat_homepage.html',{"user":request.session.get('username')})

def logout(request):
    request.session.flush()
    return render(request,'login.html')


def new_message(request):
    new_msg = request.GET.get('message')
    rakeshsanjana = db_rakesh['rakeshsanjana']
    if request.session.get('username') == 'rakesh':
        rakeshsanjana.insert_one({'sender':'rakesh','receiver':'sanjana','message':new_msg})
        doc = rakeshsanjana.find().sort("_id",-1).limit(10)
        data = []
        for msg in doc:
            data.append(msg)
        data.reverse()
        return render(request,'chat_homepage.html',{'user':request.session.get('username'),"data":data})
    else:
        rakeshsanjana.insert_one({'sender':'sanjana','receiver':'rakesh','message':new_msg})
        doc = rakeshsanjana.find().sort("_id",-1).limit(10)
        data = []
        for msg in doc:
            data.append(msg)
        data.reverse()
        return render(request,'chat_homepage.html',{'user':request.session.get('username'),"data":data})

def refresh(request):
    rakeshsanjana = db_rakesh['rakeshsanjana']
    doc = rakeshsanjana.find().sort("_id",-1).limit(10)
    data = []
    for msg in doc:
        data.append(msg)
    data.reverse()
    return render(request,'chat_homepage.html',{'user':request.session.get('username'),"data":data})
