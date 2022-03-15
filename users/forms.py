from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from . models import Profile

class UserRegisterForm(UserCreationForm):
	email = forms.EmailField(required=False)

	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']


# updating the user email and username
class UserUpdateForm(forms.ModelForm):
	email = forms.EmailField(required=False)

	class Meta:
		model = User
		fields = ['username', 'email']

# updating the user image
class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['image', 'bio','facebookLink','InstaLink','GithubLink','TwitterLink']