from django.shortcuts import render
from .models import Post

# Create your views here.

def homePageForUser(request):
	posts = Post.objects.order_by('-date')
	context = {'posts':posts}
	return render(request,'newsApp/homePageForUser.html',context)