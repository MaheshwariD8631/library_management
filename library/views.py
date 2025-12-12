from django.shortcuts import render, redirect
from .models import Book, Member, Issue

def home(request):
    return render(request, 'home.html')

def books(request):
    data = Book.objects.all()
    return render(request, 'books.html', {"data": data})

def members(request):
    data = Member.objects.all()
    return render(request, 'members.html', {"data": data})

def issue_book(request):
    books = Book.objects.filter(available=True)
    members = Member.objects.all()

    if request.method == "POST":
        book_id = request.POST['book']
        member_id = request.POST['member']

        Issue.objects.create(
            book_id=book_id,
            member_id=member_id
        )

        book = Book.objects.get(id=book_id)
        book.available = False
        book.save()

        return redirect('issued_list')

    return render(request, 'issue.html', {"books": books, "members": members})

def issued_list(request):
    data = Issue.objects.all()
    return render(request, 'issued.html', {"data": data})


# Create your views here.
