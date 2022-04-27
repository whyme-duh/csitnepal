from django.db import models
from django.contrib.auth.models import User
from PIL import Image
class Profile(models.Model):
	user = models.OneToOneField(User, on_delete= models.CASCADE)
	image = models.ImageField(default = 'default.jpg', upload_to = "profile_pic")
	bio = models.TextField(blank=True, max_length=100)
	facebookLink = models.URLField(blank=True)
	InstaLink = models.URLField(blank=True)
	GithubLink = models.URLField(blank=True)
	TwitterLink = models.URLField(blank= True)
	

	def __str__(self):
		return f'{self.user.username} Profile'

	def save(self ,*args , **kwargs): 
		super(Profile, self).save(*args , **kwargs) # saves the parent method "save"

		img = Image.open(self.image.path)
		if img.height > 300 or img.width > 300 :
			output_size = (300, 300)
			img.thumbnail(output_size)  # resize the image 
			img.save(self.image.path)