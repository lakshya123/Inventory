from django.shortcuts import render,redirect,get_object_or_404
from .forms import BookForm,BookSearch,BookEdit
from .models import Book

def home(request):
    title = 'WELCOME TO '
    context = {
        "title" : title,
    }

    return render(request,"home.html",context)

def data_entry(request):
    title = 'ADD BOOK'
    form = BookForm(request.POST or None)

    if(form.is_valid()):
        form.save()
        return redirect('/book_list')
    
    context = {
        "title" : title,
        "form" : form,
    }

    return render(request,"data_entry.html",context)

def book_list(request):
    title = 'INVENTORY'
    form = BookSearch(request.POST or None)


    querySet = Book.objects.all()
    if(request.method == 'POST'):
        querySet = Book.objects.all().filter(Title__icontains=form['Title'].value(),Author__icontains=form['Author'].value(),Subject__icontains=form['Subject'].value()
            ,Language__icontains=form['Language'].value())

    context = {
        "title" : title,
        "querySet" : querySet,
        "form" : form,
    }


    return render(request,"book_list.html",context)

def data_edit(request,id=None):
    modify = get_object_or_404(Book,id = id)
    form = BookEdit(request.POST or None, instance = modify)

    if(form.is_valid()):
        modify = form.save(commit = False)
        modify.save()
        return redirect('/book_list')
    
    context = {
        "title" : 'EDIT',
        "instance" : modify,
         "form" : form
    }

    return render(request,"data_entry.html",context)

def data_remove(request,id = None):
    modify = get_object_or_404(Book,id = id)
    modify.delete()
    return redirect('/book_list')