from __future__ import unicode_literals
from datetime import date
from django.db import models

# Create your models here.

class Post(models.Model):
	title = models.CharField(max_length=50)
	content = models.TextField()
	date = models.DateField()
	upload_image = models.ImageField(upload_to='resources/%Y/%m/%d/', null=True, blank=True)
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
    date = models.DateTimeField()
    #reply_to = models.ForeignKey(Comment, blank=True, null=True)


