from django.db import models
import re

class Anime(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    thumbnail_url = models.URLField(blank=True)
    trailer_url = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}"
    
class Episode(models.Model):
    anime = models.ForeignKey(Anime, related_name='episodes', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    episode_number = models.PositiveIntegerField()
    video_link = models.URLField()

    def __str__(self):
        return f"{self.anime.title} - Episode {self.episode_number}"

   