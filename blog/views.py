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
    
    # --context data
    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context['cat_menu'] = cat_menu
        return context

# Category list view
def categoryListView(request):
    cat_menu_list = Category.objects.all()
    return render(request, 'category_list.html', {'cat_menu_list': cat_menu_list})

# category view
def categoryView(request, cats):
    category_posts = Post.objects.filter(category=cats.replace('-', ' '))
    return render(request, 'categories.html', {'cats': cats.title().replace('-', ' '), 'category_posts': category_posts})

# Detail
class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_detail.html'
    
    # --context data
    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(ArticleDetailView, self).get_context_data(*args, **kwargs)
        context['cat_menu'] = cat_menu
        return context
    
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
    success_url = reverse_lazy('add_post')

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