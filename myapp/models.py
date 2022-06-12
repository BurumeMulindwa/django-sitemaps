from django.db import models
from django.urls import reverse


class Snippet(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('snippet_detail', args=[str(self.id)])
