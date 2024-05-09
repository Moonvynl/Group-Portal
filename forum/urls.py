from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import ListCategoriesView, CategoriesTopicsView, TopicsPostsView, PostDetailView

urlpatterns = [
    path('categories/', login_required(ListCategoriesView.as_view()), name='all-categories'),
    path('category/<int:category_id>/topics', login_required(CategoriesTopicsView.as_view()), name='topics'),
    path('topic/<int:topic_id>/posts', login_required(TopicsPostsView.as_view()), name='posts'),
    path('post/<int:pk>/', login_required(PostDetailView.as_view()), name='post-detail')
]