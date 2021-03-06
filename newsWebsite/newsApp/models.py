from __future__ import unicode_literals
from datetime import date,datetime
from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User

# Create your models here.
class cate(models.Model):
 title = models.CharField(max_length=50)
 def __str__(self):
		return self.title

class Tag(models.Model):
	tagText = models.CharField(max_length = 20)
	def __str__(self):
		return self.tagText

class Post(models.Model):
	title = models.CharField(max_length=50)
	content = RichTextUploadingField()
	date = models.DateTimeField(default = datetime.now)
	cat = models.ForeignKey(cate)
	upload_image = models.ImageField(upload_to='resources/%Y/%m/%d/')
	def __str__(self):
		return self.title
	tag = models.ManyToManyField(Tag)
	

class Comment(models.Model):
    post = models.ForeignKey(Post)
    user = models.ForeignKey(User)
    text = models.TextField()
    date = models.DateTimeField(default = datetime.now)
    def __str__(self):
		return self.text
    #reply_to = models.ForeignKey(Comment, blank=True, null=True)





