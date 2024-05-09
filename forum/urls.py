from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import ListCategoriesView, CategoriesTopicsView

urlpatterns = [
    path('categories/', login_required(ListCategoriesView.as_view()), name='all-categories'),
    path('category/<int:category_id>/topics', login_required(CategoriesTopicsView.as_view()), name='topics')
]