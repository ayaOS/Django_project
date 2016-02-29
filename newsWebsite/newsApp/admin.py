from django.contrib import admin

# Register your models here.
from .models import Post,cate
from .models import Comment,Tag


class CustomPost(admin.ModelAdmin):
	search_fields = ['title']
	list_filter = ['date']
	list_display = ('title','content','date','upload_image')

class CustomComment(admin.ModelAdmin):
	list_filter = ['date']
	list_display = ('text','date','post')


# register the models
admin.site.register(Post,CustomPost)
#admin.site.register(Comment,CustomComment)
admin.site.register(Tag)
admin.site.register(cate)


