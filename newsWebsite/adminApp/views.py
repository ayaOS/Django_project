from django.shortcuts import render , get_object_or_404
from newsApp.models import Post
from newsApp.forms import PostForm
from django.http import request , HttpResponse ,HttpResponseRedirect, Http404

# Create your views here.


def homePage(request):
	return render(request,'homePage.html',{})

def displayPosts(request):
	posts = Post.objects.order_by('-date')
	conext = {"posts":posts}
	return render(request,'displayPost.html',conext)

def newPost(request):
	form = PostForm()
	if request.method == 'POST':
		form = PostForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/adminApp/home/post')
		else:
			return HttpResponseRedirect('/adminApp/home/newPost')
	else:
		context = {'form':form}
		return render(request,'newPost.html',context)


def editPost(request , post_id):
	post = get_object_or_404( Post, id=post_id)
	if request.method == "POST":
		form = PostForm(request.POST , instance=post)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect('/adminApp/home/post')
	else:
		form = PostForm(instance=post)
		context = {'form':form}
		return render(request,'newPost.html',context)

def deletePost(request , post_id):
	post = get_object_or_404(Post , id=post_id)
	post.delete()
	return HttpResponseRedirect('/adminApp/home/post')