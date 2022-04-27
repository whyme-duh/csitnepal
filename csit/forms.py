from django import forms 

class FileFieldForm(forms.Form):
	file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

	# class Meta:
	# 	model = NoteFile
	# 	fields = ['files', ]
	# 	widget=forms.ClearableFileInput(attrs={'multiple': True})