from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.
#business logics..
def logout_info(request):
	a = Nameform(data=request.POST)
	#import pdb;pdb.set_trace()
	print "="*30
	print a
	print "="*30
	return HttpResponse(request.POST.get("first_name")+"<br/>"+request.POST.get("last_name"))


def logout(request):
	a = Nameform()
	return render(request,"logout_user.html",{'form':a})


def login_page(request):
	return render(request,"login.html") #this is used to render or send htm page to user

def validate_login(request):
	#validate username and pwd..
	#if valid show hello.html else show up a msge saying wrong credentials
	#usergiven values are fetched..
	if request.method == "POST":
		html_user = request.POST.get("Username")
		html_pwd = request.POST.get("Password")
		
		#conect to db and validate with user give values..
		get_uname = uname_pwd.objects.filter(username = html_user)
		print get_uname
		if not get_uname:
			print "username is not registered"
			return HttpResponse("Errror : You are not registered...")
		else:
			#validate pwd..
			get_pwd = uname_pwd.objects.filter(username = html_user)[0].pwd
			if get_pwd == html_pwd:
				return render(request,"hello.html",{"uname":html_user, "abcd":get_pwd})
			else:
				return HttpResponse("pwd not matching...")
		