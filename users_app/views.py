from django.shortcuts import render
from django.http import HttpResponse
from users_app.models import User, UserAge
# Create your views here.



# Lessom 129 Model template view
def viewusers (response):
    users_list=User.objects.order_by('name')
    users_dic={'users_created': users_list}
    return render (response, 'usersapp/viewusershtml.html', context=users_dic)
