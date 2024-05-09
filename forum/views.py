from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView, View
from .models import Category, Topic, Post

# Create your views here.

class ListCategoriesView(ListView):
    model = Category
    template_name = 'forum/categories.html'
    context_object_name = 'categories'


class CategoriesTopicsView(View):
    template_name = 'forum/topics.html'
    
    def get_queryset(self, **kwargs):
        category = get_object_or_404(Category, id=kwargs.get('category_id'))
        queryset = category.topics.all()

        return queryset
    
    def get(self, request, *args, **kwargs):
        category = get_object_or_404(Category, id=kwargs.get('category_id'))
        topics = self.get_queryset(**kwargs)

        context = {
            'category': category,
            'topics': topics
        }

        return render(
            request,
            self.template_name,
            context
        )
    

class TopicsPostsView(View):
    template_name = 'forum/posts.html'
    
    def get_queryset(self, **kwargs):
        topic = get_object_or_404(Topic, id=kwargs.get('topic_id'))
        queryset = topic.posts.all()

        return queryset
    
    def get(self, request, *args, **kwargs):
        topic = get_object_or_404(Topic, id=kwargs.get('topic_id'))
        posts = self.get_queryset(**kwargs)

        context = {
            'topic': topic,
            'posts': posts
        }

        return render(
            request,
            self.template_name,
            context
        )
    

class PostDetailView(DetailView):
    model = Post
    template_name = 'forum/post-detail.html'
    context_object_name = 'post'