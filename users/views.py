from django.shortcuts import render, redirect
from django.contrib import messages

from users.models import Profile 
from . forms import UserRegisterForm, ProfileUpdateForm, UserUpdateForm
from django.contrib.auth.decorators import login_required


def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, f'Your account has been created so please login.' )
			return redirect('login')
		else:
			messages.error(request, f'Details are not correct' )
	else:
		form = UserRegisterForm()

	return render(request , 'users/register.html', {'form' : form})

@login_required
def profile(request):
	# here the parameter instance will fill up the form filled with the recent username and email
	if request.method == 'POST':
		userUpdate = UserUpdateForm(request.POST, instance = request.user)
		profileUpdate= ProfileUpdateForm(request.POST, request.FILES ,instance= request.user.profile)
		if userUpdate.is_valid() and profileUpdate.is_valid():
			userUpdate.save()
			profileUpdate.save()
			messages.success(request, f'Your profile has been updated')
			return redirect('user-profile')
		else:
			messages.error(request, f'Details are not correct')
			
	else:
		userUpdate = UserUpdateForm(instance = request.user)
		profileUpdate= ProfileUpdateForm(instance = request.user.profile)

	context = {
		"userUpdate_form" :userUpdate,
		'profileUpdate_form' : profileUpdate,
	}
	
	return render(request, 'users/profile.html', context)