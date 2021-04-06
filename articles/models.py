from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    description = models.CharField(max_length=150, blank=True, null= True)

    def __str__(self):
        return self.title
