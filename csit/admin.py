from django.contrib import admin
from .models import Category, Semester,Subject, NoteFile
admin.site.register(Semester)

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
	list_display = ('title', 'semester', 'code')
	list_filter = ('semester', )
	search_field = ('code')
	prepopulated_fields = {'slug' : ('title', )}


@admin.register(NoteFile)
class NoteFileAdmin(admin.ModelAdmin):
	list_filter = ('subject','category', )

	def save_model(self , request,obj, form, change):
		obj.save()

		for file in request.FILES.getlist('file_multiple'):
			obj.notefile.create(files= file)


admin.site.register(Category)

