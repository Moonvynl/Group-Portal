from django.shortcuts import render
from auth_system.models import CustomUser
from django.views.generic import DetailView, CreateView, View, ListView
from .models import *
from .forms import PortfolioCreationForm
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.core.paginator import Paginator


class UserProfile(DetailView):
    model = CustomUser
    template_name = 'user/user_profile.html'
    context_object_name = 'userp'

    def get(self, request, *args, **kwargs):
        user_is_owner = self.get_object().id == request.user.id
        portfolio = Portfolio.objects.filter(user=self.get_object())
        user = CustomUser.objects.get(id=self.get_object().id)
        projects = Project.objects.filter(user=self.get_object())
        for project in projects:
            if project.images.count() > 1:
                for img in project.images.all():
                    print(img.image)
            else:
                if project.images.exists:
                    print(project.images.first)
        if portfolio:
            project_count = projects.count()
            return render(request, self.template_name, {'portfolio': portfolio[0], 'project_count': project_count if project_count else 0, 'user': user, 'user_is_owner': user_is_owner, 'projects':projects})
        else:
            return render(request, self.template_name, {'portfolio': None, 'user': user, 'user_is_owner': user_is_owner, 'project_count':0})


class UsersList(View):
    def get(self, request, *args, **kwargs):
        users = CustomUser.objects.all()
        paginator = Paginator(users, 5)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'user/users_list.html', {'page_obj':page_obj})


class CreatePortfolio(CreateView):
    model = Portfolio
    template_name = 'user/create_portfolio.html'
    form_class = PortfolioCreationForm
    success_url = reverse_lazy('menu:index')

    def post(self, request, *args, **kwargs):
        form = PortfolioCreationForm(request.POST)
        Portfolio.objects.create(
            first_name=form.data['first_name'],
            last_name=form.data['last_name'],
            occupation = form.data['occupation'],
            bio = form.data['bio'],
            github_url=form.data['github_url'],
            tg=form.data['tg'],
            email=form.data['email'],
            adress=form.data['adress'],
            phone=form.data['phone'],
            user=CustomUser.objects.get(id=request.user.id)
        ).save()
        return HttpResponseRedirect(self.success_url)


class DeletePortfolio(View):
    def get(self, request, *args, **kwargs):
        portfolio = Portfolio.objects.get(user=request.user)
        portfolio.delete()
        return HttpResponseRedirect(reverse_lazy('menu:index'))


class CreateProject(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'user/create_project.html')

    def post(self, request, *args, **kwargs):
        portfolio = Portfolio.objects.get(user=request.user)
        project = Project.objects.create(
            title=request.POST['title'],
            git_url=request.POST['git_url'],
            description=request.POST['description'],
            user = request.user
        ).save()
        image1 = request.FILES.get('image1')
        image2 = request.FILES.get('image2')
        image3 = request.FILES.get('image3')
        if image1:
            Image.objects.create(project=project, image=image1)
        if image2:
            Image.objects.create(project=project, image=image2)
        if image3:
            Image.objects.create(project=project, image=image3)

        portfolio.projects.add(project)
        return HttpResponseRedirect(reverse_lazy('menu:index'))


class DeleteProject(View):
    def get(self, request, *args, **kwargs):
        project = Project.objects.get(id=kwargs['pk'])
        project.delete()
        return HttpResponseRedirect(reverse_lazy('menu:index'))