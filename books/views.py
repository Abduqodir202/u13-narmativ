from django.http import HttpResponse
from django.shortcuts import render, redirect

from books.models import Books


def book_list(request):
    books = Books.objects.all()  # Queryset list [<booq1>.
    return render(request, 'books/list.html', {"books": books})


def book_detail(request, pk):
    book = Books.objects.filter(id=pk).first()
    return render(request, 'books/detail.html', {"book": book})


def book_create_form(request):
    return render(request, 'books/create.html')


def book_create(request):
    data = request.POST
    book = Books(title=data.get("title"), description=data.get("description"), price=data.get("price"))
    book.save()
    # Books.objects.create(title=data['title'], description=data['description'], price=data['price'])
    return redirect('book_list')


def book_update_forme(request, pk=None):
    book = Books.objects.filter(id=pk).first()
    return render(request, 'books/update.html', {"book": book})


def book_update(request, pk=None):
    Books.objects.filter(id=pk).update(title=request.POST.get("title"), description=request.POST.get("description"),
                                       price=request.POST.get("price"))
    return redirect('book_list')


def book_delete(request, pk=None):
    Books.objects.filter(id=pk).delete()
    return redirect('book_list')
