from __future__ import unicode_literals
from datetime import date,datetime
from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Post(models.Model):
	title = models.CharField(max_length=50)
	content = RichTextField()
	date = models.DateField()
	upload_image = models.ImageField(upload_to='resources/%Y/%m/%d/')
	def __str__(self):
		return self.title
	#image
	#tag
	
class User(models.Model):
	email = models.CharField(max_length=50)
	Name = models.CharField(max_length=50)
	phone=models.IntegerField()
	passwd=models.IntegerField()

class Comment(models.Model):
    post = models.ForeignKey(Post)
    user = models.ForeignKey(User)
    text = models.TextField()
    date = models.DateTimeField(default = datetime.now)
    def __str__(self):
		return self.text
    #reply_to = models.ForeignKey(Comment, blank=True, null=True)


