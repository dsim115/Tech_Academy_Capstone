
# movies/urls.py
from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.home, name='home'),
    path('new/', views.create_movie, name='create'),
    path('browse/', views.list_movies, name='list'),
    path('<int:pk>/', views.movie_detail, name='detail'),

    # NEW
    path('<int:pk>/edit/', views.edit_movie, name='edit'),
    path('<int:pk>/delete/', views.delete_movie, name='delete'),
]
