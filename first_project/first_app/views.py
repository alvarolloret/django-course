from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index (response):
    my_dic={'insert_me' : "Now i am coming from firstapp/index.html"}
    return render (response, 'firstapp/index.html', context=my_dic)

def help (response):
    help_dic={'insert_name' : "Pedro"}
    return render (response, 'firstapp/help.html', context=help_dic)
