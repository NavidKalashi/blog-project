from django.urls import path, include
# from . import views
from .views import HomeView, ArticleDetailView, AddPostView, UpdatePostView, DeletePostView, AddCategorytView, categoryView, categoryListView, LikeView, AddCommentView

urlpatterns = [
    # path('', views.home, name='home')
    path('', HomeView.as_view(), name='home'),
    path('article/<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    path('add-post/', AddPostView.as_view(), name='add_post'),
    path('add-category/', AddCategorytView.as_view(), name='add_category'),
    path('article/edit/<int:pk>/', UpdatePostView.as_view(), name='update_post'),
    path('article/delete/<int:pk>/', DeletePostView.as_view(), name='delete_post'),
    path('category/<str:cats>/', categoryView, name='category'),
    path('category-list/', categoryListView, name='category_list'),
    path('like/<int:pk>/', LikeView, name='like_post'),
    path('article/<int:pk>/comment/', AddCommentView.as_view(), name='add_comment'),
]
