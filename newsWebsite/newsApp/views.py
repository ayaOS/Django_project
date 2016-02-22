from django.shortcuts import render

# Create your views here.

def homePageForUser(request):
	return render(request,'newsApp/homePageForUser.html',{})