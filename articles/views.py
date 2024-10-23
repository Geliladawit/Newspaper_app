from django.shortcuts import render
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
# Create your views here.
from django.views.generic import ListView
from .models import Article
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
class ArticleListView(LoginRequiredMixin, ListView):
    model = Article
    template_name = 'article_list.html'
    login_url = 'login'
class ArticleDetailView(LoginRequiredMixin, DetailView): 
    model = Article
    template_name = 'article_detail.html'
    login_url = 'login'
class ArticleUpdateView(LoginRequiredMixin, UpdateView): 
    model = Article
    fields = ('title', 'body',)
    template_name = 'article_edit.html'
    login_url = 'login'
class ArticleDeleteView(LoginRequiredMixin, DeleteView): 
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')
    login_url = 'login'
class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    template_name = 'article_new.html'
    fields = ('title', 'body')
    login_url = 'login'
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView): # new
    model = Article
    fields = ('title', 'body',)
    template_name = 'article_edit.html'
    login_url = 'login'
    def test_func(self): # new
        obj = self.get_object()
        return obj.author == self.request.user
class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView): # new
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')
    login_url = 'login'
    def test_func(self): # new
        obj = self.get_object()
        return obj.author == self.request.user