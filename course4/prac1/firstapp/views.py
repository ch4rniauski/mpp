from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseNotFound
from .models import Book


def index(request):
    books = Book.objects.all()
    return render(request, "index.html", {"books": books})


def create(request):
    if request.method == "POST":
        book = Book()
        book.title = request.POST.get("title")
        book.author = request.POST.get("author")
        book.genre = request.POST.get("genre")
        book.year = request.POST.get("year")
        book.save()
        return HttpResponseRedirect("/")


def edit(request, id):
    try:
        book = Book.objects.get(id=id)
        if request.method == "POST":
            book.title = request.POST.get("title")
            book.author = request.POST.get("author")
            book.genre = request.POST.get("genre")
            book.year = request.POST.get("year")
            book.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, "edit.html", {"book": book})
    except Book.DoesNotExist:
        return HttpResponseNotFound("<h2>Книга не найдена</h2>")


def delete(request, id):
    try:
        book = Book.objects.get(id=id)
        book.delete()
        return HttpResponseRedirect("/")
    except Book.DoesNotExist:
        return HttpResponseNotFound("<h2>Книга не найдена</h2>")
