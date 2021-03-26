from django.urls import path

from . import views


urlpatterns = [
    path('', views.index),
    path('add_book', views.add_book),
    path('authors', views.authors),
    path('add_author', views.add_author),
    path('book', views.book),
    path('book/<int:num>', views.book),
    path('author/<int:num>', views.author),
    path('assign_book/<int:num>', views.assign_book),
    path('assign_author/<int:num>', views.assign_author)


]
