import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
author_name = "John Doe"
books_by_author = Book.objects.filter(author__name=author_name)
print("Books by", author_name, ":", [book.title for book in books_by_author])

# List all books in a library
library_name = "Central Library"
library = Library.objects.get(name=library_name)
books_in_library = library.books.all()
print("Books in", library_name, ":", [book.title for book in books_in_library])

# ✅ Retrieve the librarian for a library
librarian = Librarian.objects.get(library=library)
print("Librarian for", library_name, ":", librarian.name)
