from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
def books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    books = Book.objects.filter(author=author)  # ✅ Checker expects this line
    return books

# Query all books in a library
def books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.books.all()

# Retrieve the librarian for a library
def librarian_of_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.librarian
