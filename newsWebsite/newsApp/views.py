from django.shortcuts import render, get_object_or_404
from .models import Post , Comment

# Create your views here.

def homePageForUser(request):
	posts = Post.objects.order_by('-date')
	context = {'posts':posts}
	return render(request,'newsApp/homePageForUser.html',context)

def postDetails(request , post_id):
	post = get_object_or_404( Post, id=post_id)
	comments = Comment.objects.order_by('-date')
	context = {'post':post,'comments':comments}
	return render(request,'newsApp/postDetails.html',context)