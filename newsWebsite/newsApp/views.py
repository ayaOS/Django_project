from django.shortcuts import render

# Create your views here.

def homePageForUser(request):
	return render(request,'homePageForUser.html',{})