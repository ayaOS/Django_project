from django.contrib import admin

# Register your models here.
from .models import Post
from .models import Comment


class CustomPost(admin.ModelAdmin):
	search_fields = ['title']
	list_filter = ['date']
	list_display = ('title','content','date','upload_image')

class CustomComment(admin.ModelAdmin):
	list_filter = ['date']
	list_display = ('text','date','post')


# register the models
admin.site.register(Post,CustomPost)
admin.site.register(Comment,CustomComment)
