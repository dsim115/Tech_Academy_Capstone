from django.db import models

class WatchedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(watched=True)

class Movie(models.Model):
    GENRE_CHOICES = [
        ('ACT', 'Action'),
        ('COM', 'Comedy'),
        ('DRM', 'Drama'),
        ('HOR', 'Horror'),
        ('SCI', 'Sci‑Fi'),
        ('ANI', 'Animation'),
        ('DOC', 'Documentary'),
        ('OTH', 'Other'),
    ]

    title = models.CharField(max_length=200)                                 # CharField
    release_date = models.DateField(null=True, blank=True)                   # DateField
    runtime_minutes = models.PositiveIntegerField(null=True, blank=True)     # IntegerField
    genre = models.CharField(max_length=3, choices=GENRE_CHOICES, default='OTH')
    watched = models.BooleanField(default=False)                              # BooleanField
    notes = models.TextField(blank=True)                                      # TextField
    rating = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)  # DecimalField (e.g., 8.5)
    created_at = models.DateTimeField(auto_now_add=True)                      # DateTimeField

    # Managers
    objects = models.Manager()
    watched_items = WatchedManager()

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title
