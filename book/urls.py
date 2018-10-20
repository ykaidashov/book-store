from django.urls import path

from book import views

urlpatterns = [
    path('', views.index, name='book_index_url'),
]
