from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView, View
from .models import Category

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
        print("Topics:", topics)
        context = {
            'category': category,
            'topics': topics
        }

        return render(
            request,
            self.template_name,
            context
        )