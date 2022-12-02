from django.urls import path
from .views import *

urlpatterns = [
<<<<<<< HEAD
   
    path('', index, name='home'),
    path('article/new/', article_create, name='create'),
    path('api/category/create/', category_create, name='cat_create'),
    path('api/tag/create/', tag_create, name='tag_create'),
=======
    path('', landing, name='landing'),
    path('home/', index, name='home'),
    path('api/category/create/', category_create, name='cat_create'),
    path('api/tag/create/', tag_create, name='tag_create'),
    path('api/image/upload/', image_upload, name='image_create'),
    path('article/new/', article_create, name='create'),
>>>>>>> a4e72cc6e7ea4bc2506acafb89b76e925cab4308
    path('article/<int:id>/view/', article_view, name='view'),
    path('article/search/', search_article, name='search'),
]