from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import ListCategoriesView, CategoriesTopicsView, TopicsPostsView, PostDetailView, CategoryCreateView, TopicCreateView, CategoryUpdateView, TopicUpdateView, PostUpdateView, CategoryDeleteView, TopicDeleteView, PostDeleteView

#comment for test

urlpatterns = [
    path('categories/', ListCategoriesView.as_view(), name='all-categories'),
    path('category/<int:category_id>/topics', CategoriesTopicsView.as_view(), name='topics'),
    path('topic/<int:topic_id>/posts', TopicsPostsView.as_view(), name='posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('category/create/', CategoryCreateView.as_view(), name='create-category'),
    path('category/<int:category_id>/topic/create/', TopicCreateView.as_view(), name='create-topic'),
    path('category/<int:pk>/update/', CategoryUpdateView.as_view(), name='update-category'),
    path('topic/<int:pk>/update/', TopicUpdateView.as_view(), name='update-topic'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='update-post'),
    path('category/<int:pk>/delete/', CategoryDeleteView.as_view(), name='delete-category'),
    path('topic/<int:pk>/delete/', TopicDeleteView.as_view(), name='delete-topic'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='delete-post')
]