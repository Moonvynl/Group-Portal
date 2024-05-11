from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import ListCategoriesView, CategoriesTopicsView, TopicsPostsView, PostDetailView, CategoryCreateView, TopicCreateView, CategoryUpdateView, TopicUpdateView, PostUpdateView, CategoryDeleteView, TopicDeleteView, PostDeleteView

urlpatterns = [
    path('categories/', login_required(ListCategoriesView.as_view()), name='all-categories'),
    path('category/<int:category_id>/topics', login_required(CategoriesTopicsView.as_view()), name='topics'),
    path('topic/<int:topic_id>/posts', login_required(TopicsPostsView.as_view()), name='posts'),
    path('post/<int:pk>/', login_required(PostDetailView.as_view()), name='post-detail'),
    path('category/create/', login_required(CategoryCreateView.as_view()), name='create-category'),
    path('category/<int:category_id>/topic/create/', login_required(TopicCreateView.as_view()), name='create-topic'),
    path('category/<int:pk>/update/', login_required(CategoryUpdateView.as_view()), name='update-category'),
    path('topic/<int:pk>/update/', login_required(TopicUpdateView.as_view()), name='update-topic'),
    path('post/<int:pk>/update/', login_required(PostUpdateView.as_view()), name='update-post'),
    path('category/<int:pk>/delete/', login_required(CategoryDeleteView.as_view()), name='delete-category'),
    path('topic/<int:pk>/delete/', login_required(TopicDeleteView.as_view()), name='delete-topic'),
    path('post/<int:pk>/delete/', login_required(PostDeleteView.as_view()), name='delete-post')
]