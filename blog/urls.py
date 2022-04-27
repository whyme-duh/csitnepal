from django.http import request
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static 


from . views import (PostListView,
				PostDetailView,
				CreatePostView,
				UpdatePostView, 
				PostDeleteView,
				UserPostListView,
				LoginUserPost,
				CommentView,
				BlogListView,
				CreateBlogView,
				UpdateBlogView,
				BlogDeleteView,
				BlogDetailView,
				
				
			)
from .import views 

urlpatterns = [
	path('posts/' , PostListView.as_view(), name = 'blog-home'),
	path('blogs/' , BlogListView.as_view(), name = 'blogs'),
	path('user/<str:username>' , UserPostListView.as_view(), name = 'user-post'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/create/', CreatePostView.as_view(), name='post-create'),
    path('blog/create/', CreateBlogView.as_view(), name='blog-create'),
    path('post/<int:pk>/update/', UpdatePostView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
	# path('like/<int:pk>', LikeView, name = "like_blog"),
	path('userpost/', LoginUserPost.as_view(), name = "user-post"),
    path('blog/<slug:slug>/', BlogDetailView.as_view(), name='blog-detail'),
	path('blog/<int:pk>/update/', UpdateBlogView.as_view(), name='blog-update'),
    path('blog/<int:pk>/delete/', BlogDeleteView.as_view(), name='blog-delete'),
	path('post/<int:pk>/comment',CommentView.as_view(), name='post-detail-comment'),
	path('blog/<int:pk>/comment',CommentView.as_view(), name='blog-detail-comment'),
	
]

