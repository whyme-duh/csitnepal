from django.contrib import admin
from django.db.models import query
from .models import Comments, Post,  Blog

# here we create a POst model

admin.site.register(Post)
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
	list_display = ('title','author',)
	list_filter = ('title', )
	prepopulated_fields = {"slug": ("title",)}



@admin.register(Comments)
class CommentAdmin(admin.ModelAdmin):
	list_display = ('body', 'post', 'created', 'active')
	list_filter = ('active', 'created')
	search_field = ('body')
	actions = ['approve_comments']


	def approve_comments(self, request ,queryset):
		queryset.update(active = True)

