import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
def get_books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    books = Book.objects.filter(author=author)
    for book in books:
        print(book.title)

# List all books in a library
def list_books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    for book in library.books.all():
        print(book.title)

# Retrieve the librarian for a library
def get_librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    print(library.librarian.name)


if __name__ == "__main__":
    # Optional test data (to check queries)
    author = Author.objects.create(name="George Orwell")
    book1 = Book.objects.create(title="1984", author=author)
    book2 = Book.objects.create(title="Animal Farm", author=author)
    library = Library.objects.create(name="Central Library")
    library.books.add(book1, book2)
    librarian = Librarian.objects.create(name="Ahmad", library=library)

    print("Books by author:")
    get_books_by_author("George Orwell")

    print("\nBooks in library:")
    list_books_in_library("Central Library")

    print("\nLibrarian for library:")
    get_librarian_for_library("Central Library")
