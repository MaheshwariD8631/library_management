from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('books/', views.books, name='books'),
    path('members/', views.members, name='members'),
    path('issue/', views.issue_book, name='issue_book'),
    path('issued/', views.issued_list, name='issued_list'),
]
