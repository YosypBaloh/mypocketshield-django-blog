from django.shortcuts import render
from .models import News
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView
)
from django.contrib.auth.mixins import LoginRequiredMixin



class ShowNewsView(ListView):
    model = News
    template_name = 'blog/home.html'
    context_object_name = 'news'
    ordering = ['-date']

    def get_context_data(self, **kwards):
        ctx = super(ShowNewsView, self).get_context_data(**kwards)
    
        ctx['title'] = 'Főoldal'
        return ctx

class NewsDetailView(DetailView):
    model = News

    def get_context_data(self, **kwards):
        ctx = super(NewsDetailView, self).get_context_data(**kwards)
    
        # ctx['title'] = News.objects.get(pk=self.kwargs['pk'])
        ctx['title'] = self.object.title
        return ctx

class UpdateNewsView(LoginRequiredMixin, UpdateView):
    model = News
    template_name = 'blog/create_news.html'

    fields = ['title', 'text']

    def get_context_data(self, **kwards):
        ctx = super(UpdateNewsView, self).get_context_data(**kwards)
    
        ctx['title'] = 'Bejegyzés frissítése'
        ctx['btn_text'] = 'Frissítse a bejegyzést'
        return ctx

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class CreateNewsView(LoginRequiredMixin, CreateView):
    model = News
    template_name = 'blog/create_news.html'

    fields = ['title', 'text']

    def get_context_data(self, **kwards):
        ctx = super(CreateNewsView, self).get_context_data(**kwards)
    
        ctx['title'] = 'Bejegyzés hozzáadása'
        ctx['btn_text'] = 'Adja hozzá a bejegyzést'
        return ctx

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

def contacts(request):
    return render(request, 'blog/contacts.html', {'title':'Kapcsolat oldal!'})
