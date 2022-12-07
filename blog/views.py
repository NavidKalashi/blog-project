from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Post, Category
from .forms import PostForm, EditPost

# Create your views here.

# def home(request):
    # return render(request, 'home.html', {})

# Home
class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-date']
    # ordering = ['-id']

def CategoryView(request, cats):
    category_posts = Post.objects.filter(category=cats)
    return render(request, 'categories.html', {'cats': cats.title(), 'category_posts': category_posts})

# Detail
class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_detail.html'
    
# Add
class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    # fields = '__all__'

# Category
class AddCategorytView(CreateView):
    model = Category
    # form_class = PostForm
    template_name = 'add_category.html'
    fields = '__all__'

# Update
class UpdatePostView(UpdateView):
    model = Post
    form_class = EditPost
    template_name = 'update_post.html'
    # fields = ['title', 'title_tag', 'body']
    
# Delete
class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')