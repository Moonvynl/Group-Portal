from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, View, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator
from django.core.exceptions import PermissionDenied
from django.core.paginator import Paginator
from .models import Category, Topic, Post
from .forms import CategoryCreationForm, TopicCreationForm, PostCreationForm, CategoryUpdateForm, TopicUpdateForm, PostUpdateForm
from .mixins import CreatorIsOwnerMixin, AuthorIsOwnerMixin

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

        paginator = Paginator(topics, 5)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context = {
            'category': category,
            'topics': topics,
            'page_obj': page_obj
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

        paginator = Paginator(posts, 5)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context = {
            'topic': topic,
            'posts': posts,
            'form': form,
            'page_obj': page_obj
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
            return redirect('forum:posts', topic_id=topic_id)
        
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
    success_url = reverse_lazy('forum:all-categories')


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
            return redirect('forum:topics', category_id=category_id)
        
        return render(
            request,
            self.template_name,
            context
        )
    
@method_decorator(user_passes_test(is_user_moderator_or_admin), name='dispatch')
class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryUpdateForm
    template_name = 'forum/category-update.html'
    success_url = reverse_lazy('forum:all-categories')


class TopicUpdateView(CreatorIsOwnerMixin, UpdateView):
    model = Topic
    form_class = TopicUpdateForm
    template_name = 'forum/topic-update.html'
    
    def get_success_url(self) -> str:
        category_id = self.object.category_id
        return reverse_lazy('forum:topics', kwargs={'category_id': category_id})
    

class PostUpdateView(AuthorIsOwnerMixin, UpdateView):
    model = Post
    form_class = PostUpdateForm
    template_name = 'forum/post-update.html'

    def dispatch(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
    
    def get_success_url(self) -> str:
        topic_id = self.object.topic_id
        return reverse_lazy('forum:posts', kwargs={'topic_id': topic_id})
    

@method_decorator(user_passes_test(is_user_moderator_or_admin), name='dispatch')
class CategoryDeleteView(DeleteView):
    model = Category
    success_url = reverse_lazy('forum:all-categories')


class TopicDeleteView(CreatorIsOwnerMixin, DeleteView):
    model = Topic

    def get_success_url(self) -> str:
        category_id = self.object.category_id
        return reverse_lazy('forum:topics', kwargs={'category_id': category_id})
    

class PostDeleteView(AuthorIsOwnerMixin, DeleteView):
    model = Post

    def get_success_url(self) -> str:
        topic_id = self.object.topic_id
        return reverse_lazy('forum:posts', kwargs={'topic_id': topic_id})