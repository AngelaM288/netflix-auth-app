from django.urls import path
from .views import MovieListView

urlpatterns = [
    path('', MovieListView.as_view()),  # ruta vacía porque el prefijo ya está en backend.urls
]
