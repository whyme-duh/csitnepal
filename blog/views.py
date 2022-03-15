from blog.forms import CommentForm
from .models import Blog, Comments,  Post
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.models import User
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView, 
    UpdateView,
    DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required

context = {
        "posts" : Post.objects.all(),
        
    }


class BlogListView(ListView):
    model = Blog
    ordering = ["-datePosted"]
    paginate_by = 5
    context_object_name = "blogs"

class BlogDetailView(DetailView):
    model = Blog

class CreateBlogView(LoginRequiredMixin, CreateView):
    # creates post searches for the template based on the naming => <app>/<model>_<viewtype>.html
    # blog_form.html is being used in this and updatepost view
    
    model = Blog    
    fields = ['title', 'content']
    success_url = '/blogs'


    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class UpdateBlogView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Blog    
    fields = ['title', 'content']
    success_url = '/blogs'


    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # is the method to check whether the user passes the test, 
    def test_func(self):
        blog = self.get_object()
        if (self.request.user == blog.author ):
            return True
        return False

class BlogDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Blog
    # this solves the issue for the success url while not providing it at first 
    # it just redirects the url to home page after the deletion
    success_url = '/userpost'

    # is the method to check whether the user passes the test, 
    def test_func(self):
        blog = self.get_object()
        if (self.request.user == blog.author ):
            return True
        return False

class PostListView(ListView):
    model = Post
    template_name = 'blog/useruploads.html' # <app>/<model>_<viewtype>.html    
    context_object_name = "posts"
    ordering = ["-datePosted"]
    paginate_by = 5

class UserPostListView(ListView):
    model = Post, User
    template_name = 'blog/user_posts.html' # <app>/<model>_<viewtype>.html    
    context_object_name = "posts"
    ordering = ["-datePosted"]
    paginate_by =5
        
    

    # to change the url on the basis of the username of the user 
    # we override the existing function
    def get_queryset(self):
        user = get_object_or_404(User, username = self.kwargs.get('username'))
        return Post.objects.filter(author = user).order_by('-datePosted')



class PostDetailView( DetailView ):
    model = Post


    

# used for the comments on the detail page
def post_detail(request, slug):
    template_name = 'blog/post_detail.html'
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        form = CommentForm(data=request.POST)
        if form.is_valid():
            

            # Create Comment object but don't save to database yet
            new_comment = form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
            return redirect('/' + post.slug)
    else:
        form = CommentForm()
    context = {
        'post': post,
        'comments': comments,
        'new_comment': new_comment,
        'form': form}
    return render(request, template_name, context)

class CommentView( CreateView):
    # creates post searches for the template based on the naming => <app>/<model>_<viewtype>.html
    # post_form.html is being used in this and updatepost view
    
    model = Comments    
    fields = ['name', 'email', 'body']


    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    

                                               
class CreatePostView(LoginRequiredMixin, CreateView):
    # creates post searches for the template based on the naming => <app>/<model>_<viewtype>.html
    # post_form.html is being used in this and updatepost view
    
    model = Post    
    fields = ['title', 'content', 'files']
    success_url = '/posts'


    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

   



class UpdatePostView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post    
    fields = ['title', 'content', 'files']
    success_url = '/posts'
    

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # is the method to check whether the user passes the test, 
    # gonna check if the current user is the author of the post
    def test_func(self):
        post = self.get_object()
        if (self.request.user == post.author ):
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    # this solves the issue for the success url while not providing it at first 
    # it just redirects the url to home page after the deletion
    success_url = '/'

    # is the method to check whether the user passes the test, 
    def test_func(self):
        post = self.get_object()
        if (self.request.user == post.author ):
            return True
        return False

  



# this function is used for displaying the user's post

class LoginUserPost(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'blog/my_post.html' # <app>/<model>_<viewtype>.html    
    context_object_name = "posts"
    ordering = ["-datePosted"]
    paginate_by =5

    def get_context_data(self, **kwargs):
        context= super(LoginUserPost, self).get_context_data(**kwargs)
        context.update({
            'blogs' : Blog.objects.all(),
        })
        return context


