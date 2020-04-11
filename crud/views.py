from django.shortcuts import render, redirect
from crud.models import Books
from django.utils.datastructures import MultiValueDictKeyError

def index(request):
   books = Books.objects.all()
   book = {'books':books}
   return render(request, 'base.html', book)

def to_update(request):
   books = Books.objects.all()
   book = {'books': books}
   return render(request, 'update.html', book)

def to_delete(request):
   books = Books.objects.all()
   book = {'books': books}
   return render(request, 'delete.html', book)

def create(request):
   books = Books(name=request.POST['name'],author=request.POST['author'], price=request.POST['price'])
   books.save()
   return redirect('/')

def edit(request,id):
   books=Books.objects.get(id=id)
   book = {'books': books}
   return render(request, 'edit.html', book)

def update(request, id):
   books=Books.objects.get(id=id)
   books.name = request.POST.get('name')
   books.author = request.POST.get('author')
   books.price = request.POST.get('price')
   books.save()
   return redirect('/')

def delete(request, id):
   books = Books.objects.get(id=id)
   books.delete()
   return redirect('/')

