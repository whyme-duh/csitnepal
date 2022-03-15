from pickle import FALSE
from django.db import models
from django.db.models.fields import TextField
from django.utils import timezone
from django.contrib.auth.models import User

from django.utils.text import slugify
from django.urls import reverse
from django import forms
from ckeditor.fields import RichTextField


class Post(models.Model):
	title = models.CharField(max_length= 100)
	content = RichTextField(blank = False, null = False)
	datePosted = models.DateTimeField(default= timezone.now)
	likes = models.IntegerField(default= 0)
	
	# as one post have only one user but one user might have multiple posts
	author = models.ForeignKey(User, on_delete= models.CASCADE)
	files = models.FileField(upload_to= "files/", blank= False )
	# prints the post object the way we want
	def __str__(self):
		return self.title

	def get_absolute_url(self):
		# return reverse('post-detail', kwargs= {'pk': self.pk})
		return reverse('blog-home')

class Blog(models.Model):
	title = models.CharField(max_length= 100)
	content = RichTextField(blank = False, null = False)

	datePosted = models.DateTimeField(default= timezone.now)
	likes = models.IntegerField(default= 0)
	
	# as one post have only one user but one user might have multiple posts
	author = models.ForeignKey(User, on_delete= models.CASCADE)
	# prints the post object the way we want
	def __str__(self):
		return f'{self.title} created by {self.author} on {self.datePosted}.'

	def get_absolute_url(self):
		# return reverse('post-detail', kwargs= {'pk': self.pk})
		return reverse('blog-home')

class Comments(models.Model):
	post = models.ForeignKey(Post, on_delete= models.CASCADE, related_name= "comments", null=True, blank=True)
	blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name = "blog_comments", null = True, blank = True)
	name = models.CharField(max_length=80, blank= True)
	email = models.EmailField(blank = True)
	body = models.TextField()
	created =  models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now= True)
	active = models.BooleanField(default=True)

	class Meta:
		ordering = ('created',)

	def __str__(self):
		return 'Comment by {} on {}'.format(self.name, self.post)

	def get_absolute_url(self):
		return reverse('blog-detail', kwargs={'pk' : self.pk})


