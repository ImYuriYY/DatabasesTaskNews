from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='homepage'),
    path('create/', create, name='create'),
    path('author/<int:id>', author, name='author'),
    path('edit/<int:id>/', edit, name='edit'),
    path('delete/<int:id>/', delete, name='delete')
]