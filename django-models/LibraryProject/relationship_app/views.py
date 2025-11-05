from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import Book, Library

# Function-Based View
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-Based View: ListView of books in a specific library
class LibraryBooksView(ListView):
    model = Book
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'books'

    def get_queryset(self):
        library = get_object_or_404(Library, pk=self.kwargs['pk'])
        return Book.objects.filter(library=library)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['library'] = get_object_or_404(Library, pk=self.kwargs['pk'])
        return context
