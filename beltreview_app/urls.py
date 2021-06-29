from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('login', views.login),
    path('logout', views.logout),
    path('books', views.books),
    path('add', views.add),
    path('addbook', views.addbook),
    path('books/<int:book_id>', views.aboutbooks),
]