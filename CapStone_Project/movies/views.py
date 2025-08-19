# movies/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q

from .forms import MovieForm
from .models import Movie


def home(request):
    """Landing page for the Movies app — shows a small recent list."""
    movies = Movie.objects.all().order_by('-created_at')[:10]
    return render(request, 'movies/home.html', {'movies': movies})


def create_movie(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            movie = form.save()
            messages.success(request, f'“{movie.title}” was added to your collection.')
            return redirect('movies:home')
        messages.error(request, 'Please correct the errors below.')
    else:
        form = MovieForm()
    return render(request, 'movies/movie_form.html', {'form': form})


def list_movies(request):
    q = request.GET.get('q', '').strip()
    qs = Movie.objects.all()

    if q:
        qs = qs.filter(Q(title__icontains=q) | Q(notes__icontains=q))

    sort_param = request.GET.get('sort', '-created')
    sort_map = {
        'title': 'title', '-title': '-title',
        'release': 'release_date', '-release': '-release_date',
        'rating': 'rating', '-rating': '-rating',
        'created': 'created_at', '-created': '-created_at',
    }
    qs = qs.order_by(sort_map.get(sort_param, '-created_at'))

    paginator = Paginator(qs, 6)
    page_obj = paginator.get_page(request.GET.get('page'))

    return render(request, 'movies/movie_list.html', {
        'page_obj': page_obj,
        'q': q,
        'sort': sort_param,
        'paginator': paginator,
        'total_count': paginator.count,
    })


def movie_detail(request, pk):
    m = get_object_or_404(Movie, pk=pk)
    return render(request, 'movies/movie_detail.html', {'m': m})


def edit_movie(request, pk):
    """Update an existing movie."""
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == 'POST':
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            messages.success(request, f'“{movie.title}” was updated.')
            return redirect('movies:detail', pk=movie.pk)
        messages.error(request, 'Please correct the errors below.')
    else:
        form = MovieForm(instance=movie)

    return render(request, 'movies/movie_form.html', {
        'form': form,
        'is_edit': True,
        'movie': movie,
    })


def delete_movie(request, pk):
    """Delete with a simple confirm step (POST)."""
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == 'POST':
        title = movie.title
        movie.delete()
        messages.success(request, f'“{title}” was deleted.')
        return redirect('movies:list')

    # Fallback GET confirm page (ok to keep even if you use a modal on detail page)
    return render(request, 'movies/movie_confirm_delete.html', {'m': movie})
