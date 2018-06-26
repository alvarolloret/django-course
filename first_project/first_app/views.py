from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import AccesRecord, Topic, Webpage
# Create your views here.

def index (response):
    my_dic={'insert_me' : "Now i am coming from firstapp/index.html"}
    return render (response, 'firstapp/index.html', context=my_dic)

def help (response):
    help_dic={'insert_name' : "Pedro"}
    return render (response, 'firstapp/help.html', context=help_dic)

def photo (response):
        return render (response, 'firstapp/photo.html')

# Lessom 129 Model template view
def mtv (response):
    webpages_list=AccesRecord.objects.order_by('date')
    date_dic={'acces_records': webpages_list}
    return render (response, 'firstapp/mtv.html', context=date_dic)
