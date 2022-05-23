from cgi import print_arguments
import imp
from multiprocessing import context
from pdb import line_prefix
import re
from django.shortcuts import render , redirect
from .models import employee
from usermanagementapp import paths
from datetime import datetime
import os
# Create your views here.

file = paths.folder

def read(request):
    return render(request,'test.html')

def index(request):
    e = employee('rakesh','cse')
    l = [e]
    with open(file,'r') as f:
        lines = f.readlines()
    # print(lines)
    context= {
        'current_list' : l,
        'lines' : lines
    }
    return render(request,'index.html',context)


def adduser(request):
    newuser = request.POST['username']
    print(newuser)
    with open(file,'a+') as f:
        timestamp = str(datetime.now())
        f.write(str(newuser)+timestamp+'\n')
        f.seek(0)
        lines = f.readlines()
    # print(file)
    
    e = employee('rakesh','cse')
    l = [e]
    context= {
        'current_list' : l,
        'lines' : lines
    }
    return render(request,'index.html',context)


def deleteuser(request,line):
    newuser = line
    with open(file,'r') as f:
        lines = f.readlines() 
    print(lines)

    new_lines = []
    for l in lines:
        if l != line:
            new_lines.append(l)
        # else:
        #     # print("found the line: "+l)

    # open(file,'w').close()
    with open(file,'r+') as f:
        f.truncate(0)

    with open(file,'w') as f:
        for l in new_lines:
            f.write(l)
    # print("line is : " + newuser)
    print(new_lines)

    with open(file,'r') as f:
        liness = f.readlines()
    print(liness)
    context = {
        'lines' : liness
    }
    return render(request,'index.html',context)

def edituser(request):
    line = request.POST.get('data')
    l = request.POST.get('username')
    print(line)
    print(l)
    with open(file,'r') as f:
        lines = f.readlines()
    # line = line+"\n"
    # i = lines.index(line)
    # lines[i] = 
    # for l in lines:
    #     if l == line:

    # print(line)
    return render(request,'index.html',context={"lines" : lines})

