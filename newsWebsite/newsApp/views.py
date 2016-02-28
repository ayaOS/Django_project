from django.shortcuts import render, get_object_or_404
from .models import Post , Comment ,Tag
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect,HttpResponse
from django.template import RequestContext
from newsApp.forms import *
# Create your views here.
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def listing(request):
    post_list = Post.objects.order_by('-date')
    #post_list = Post.objects.all()
    paginator = Paginator(post_list, 5) # Show 2 contacts per page

    page_num = request.GET.get('page')
    try:
        posts = paginator.page(page_num)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        posts = paginator.page(paginator.num_pages)

    return render(request, 'newsApp/homePageForUser.html', {'posts': posts})

#def homePageForUser(request):
#	posts = Post.objects.order_by('-date')
#	context = {'posts':posts}
#	return render(request,'newsApp/homePageForUser.html',context)

def postDetails(request , post_id):
	post = get_object_or_404( Post, id=post_id)
	comments = Comment.objects.filter(post=post_id)
   # tags = Post.objects.filter ()
	context = {'post':post,'comments':comments}
	return render(request,'newsApp/postDetails.html',context)



@csrf_protect
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1'],
            email=form.cleaned_data['email']
            )
            return HttpResponseRedirect('/register/success/')
    else:
        form = RegistrationForm()
    variables = RequestContext(request, {
    'form': form
    })
   
    return render_to_response(
    'registration/register.html',
    variables,
    )
 
def register_success(request):
    return render_to_response(
    'registration/success.html',
    )
 
def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')



