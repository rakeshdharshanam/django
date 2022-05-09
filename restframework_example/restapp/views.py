from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from pymongo import MongoClient
from googletrans import Translator
from bson.json_util import dumps 
import json
# Create your views here.

connection = MongoClient('localhost',27017)
db_rakesh = connection['rakesh']
collection_rakeshsanjana = db_rakesh['users']

@api_view(['GET'])
def start(request):
    results = dumps(collection_rakeshsanjana.find())
    results = json.loads(results)
    return Response(results)

@api_view(['GET'])
def user_name(request,name):
    results = dumps(collection_rakeshsanjana.find({"username":name}))
    results = json.loads(results)
    return Response(results)


@api_view(['POST'])
def check_post(request):
    data = request.data
    print(type(data))
    ans = int(data['num1']) * int(data['num2'])
    return Response({"received" : ans})

@api_view(['POST'])
def translate_to_telugu(request):
    translator = Translator()
    data = request.data 
    print(data)
    result = {}
    t  = translator.translate(data['msg'],dest = 'te')
    print(t.text)
    # result = dumps(result)
    # result = json.loads(result)
    return Response({"msg" : t.text})
    
