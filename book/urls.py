from django.urls import path

from book import views

urlpatterns = [
    path('', views.index, name='book_index_url'),
    path('book/create', views.BookCreate.as_view(), name='book_create_url'),
    path('book/<int:book_id>/update', views.BookUpdate.as_view(), name='book_update_url')
]
