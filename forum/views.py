from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, View, CreateView
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator
from .models import Category, Topic, Post
from .forms import CategoryCreationForm, TopicCreationForm, PostCreationForm

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
    form_class = PostCreationForm
    
    def get_queryset(self, **kwargs):
        topic = get_object_or_404(Topic, id=kwargs.get('topic_id'))
        queryset = topic.posts.all()

        return queryset
    
    def get(self, request, *args, **kwargs):
        topic = get_object_or_404(Topic, id=kwargs.get('topic_id'))
        posts = self.get_queryset(**kwargs)
        form = self.form_class

        context = {
            'topic': topic,
            'posts': posts,
            'form': form
        }

        return render(
            request,
            self.template_name,
            context
        )
    
    def post(self, request, *args, **kwargs):
        topic = Topic.objects.get(id=kwargs.get('topic_id'))
        form = self.form_class(request.POST)

        context = {
            'topic': topic,
            'form': form
        }

        if form.is_valid():
            form.instance.author_id = self.request.user.id
            topic_id = kwargs.get('topic_id')
            topic = Topic.objects.get(id=topic_id)
            post = form.save(commit=False)
            post.topic = topic
            post.save()
            topic.posts.add(post)
            return redirect('posts', topic_id=topic_id)
        
        return render(
            request,
            self.template_name,
            context
        )
    

class PostDetailView(DetailView):
    model = Post
    template_name = 'forum/post-detail.html'
    context_object_name = 'post'


def is_user_moderator_or_admin(user):
    return user.is_authenticated and (user.access == 'moder' or user.is_staff)


@method_decorator(user_passes_test(is_user_moderator_or_admin), name='dispatch')
class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryCreationForm
    template_name = 'forum/category-creation.html'
    success_url = reverse_lazy('all-categories')


class TopicCreateView(View):
    template_name = 'forum/topic-creation.html'
    form_class = TopicCreationForm

    def get(self, request, *args, **kwargs):
        category = Category.objects.get(id=kwargs.get('category_id'))
        form = self.form_class

        context = {
            'category': category,
            'form': form
        }

        return render(
            request,
            self.template_name,
            context
        )

    def post(self, request, *args, **kwargs):
        category = Category.objects.get(id=kwargs.get('category_id'))
        form = self.form_class(request.POST)

        context = {
            'category': category,
            'form': form
        }

        if form.is_valid():
            form.instance.creator_id = self.request.user.id
            category_id = kwargs.get('category_id')
            category = Category.objects.get(id=category_id)
            topic = form.save(commit=False)
            topic.category = category
            topic.save()
            category.topics.add(topic)
            return redirect('topics', category_id=category_id)
        
        return render(
            request,
            self.template_name,
            context
        )