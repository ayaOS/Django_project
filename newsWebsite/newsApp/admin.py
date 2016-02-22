from django.contrib import admin

# Register your models here.
from .models import Post
from .models import Comment
from .models import User
# register the models
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(User)