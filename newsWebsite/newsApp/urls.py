from . import views
from django.conf.urls import url 

urlpatterns = [

	url(r'^home$',views.listing),
	#url(r'^home$',views.homePageForUser),

	url(r'^home/post/(?P<post_id>[0-9]+)',views.postDetails),
	url(r'^cat/(?P<cat_id>[0-9]+)$',views.categry),


	
        
]


