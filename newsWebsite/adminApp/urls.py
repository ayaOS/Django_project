from . import views
from django.conf.urls import url 

urlpatterns = [
	url(r'^home$',views.homePage),
	url(r'^home/post',views.displayPosts),
	url(r'^home/newPost$',views.newPost),
	url(r'^home/editPost/(?P<post_id>[0-9]+)$',views.editPost),
	url(r'^home/deletePost/(?P<post_id>[0-9]+)$',views.deletePost)

]