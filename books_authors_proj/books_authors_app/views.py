from django.shortcuts import HttpResponse, redirect, render
from .models import Book, Author


def index(request):
    books = Book.objects.all()
    context = {
        "books": books
    }
    return render(request, "index.html", context)


def add_book(request):
    Book.objects.create(
        title=request.POST["title"],
        desc=request.POST["desc"]
    )
    return redirect("/")


def authors(request):
    authors = Author.objects.all()
    context = {
        "authors": authors
    }
    return render(request, "authors.html", context)


def add_author(request):
    Author.objects.create(
        first_name=request.POST["first_name"],
        last_name=request.POST["last_name"],
        notes=request.POST["notes"]
    )
    return redirect("author.html")


def book(request, num):
    print('***************id sent****************')
    print(num)
    book = Book.objects.get(id=num)
    author = Author.objects.all()
    print('*********book*******')
    print(book)
    context = {
        "book": book,
        "authors": author
    }
    return render(request, "book.html", context, num)


def author(request, num):
    books = Book.objects.all
    author = Author.objects.get(id=num)

    context = {
        "books": books,
        "author": author
    }
    return render(request, "author.html", context, num)


def assign_book(request, num):
    print(num)
    this_book = Book.objects.get(id=request.POST["book_id"])
    print('**************this book******')
    print(this_book)
    this_author = Author.objects.get(id=num)
    print('**************this author******')
    print(this_author)

    this_book.authors.add(this_author)

    return redirect('/')


def assign_author(request, num):
    print(num)
    this_author = Author.objects.get(id=request.POST["author_id"])
    print('**************this author******')
    print(this_author)
    this_book = Book.objects.get(id=num)
    print('**************this book******')
    print(this_book)

    this_author.books.add(this_book)

    return redirect('/')
