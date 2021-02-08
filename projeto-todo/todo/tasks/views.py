from django.shortcuts import render
from django.http import HttpResponse

def helloword(request):
    return HttpResponse('Hello Word')

def tasklist (request):
    return render(request,'tasks/list.html')

def yourName(request,name):
    return render(request,'tasks/yourname.html',{'name':name})