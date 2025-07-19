# users/urls.py

from django.urls import path
from .views import RegisterView  # Importamos tu vista

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
]
