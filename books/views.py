from django.db.models import Q
from django.shortcuts import render
from .models import Book
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.views.generic import ListView , DetailView

class BookListView(LoginRequiredMixin,ListView):
    model = Book
    context_object_name = 'book_list' # renaming my object list to make it friendlier
    template_name = 'books/book_list.html'
    login_url = 'account_login' # permissions for only a logged in user to see books and a url to logon if not 

class BookDetailView(LoginRequiredMixin,PermissionRequiredMixin,DetailView):
    model=Book
    context_object_name = 'book'
    template_name = 'books/book_detail.html'
    login_url = 'account_login'
    permission_required = 'books.special_status' 

class SearchResultsListView(ListView):
    model=Book
    context_object_name = 'book_list'
    template_name ='books/book_results.html'
    
    def get_queryset(self):
        query = self.request.GET.get('q')
        return Book.objects.filter(
            Q(title__icontains = query) | Q(author__icontains = query))
        

       
        
