from time import time
from django.shortcuts import render
from datetime import datetime
from rest_framework.decorators import api_view
from rest_framework.response import Response
from bson.json_util import dumps
import json
# Create your views here.
@api_view(['GET'])
def kmrtime(request):
    current_time = datetime.now()
    time_now = current_time.strftime("%H:%M:%S")
    time_now = dumps(time_now)
    time_now = json.loads(time_now)
    print(time_now)
    return Response(time_now)