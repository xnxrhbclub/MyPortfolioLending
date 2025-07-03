from django.db import models

class GitHubProject(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    url = models.URLField()
    stars = models.IntegerField(default=0)
    language = models.CharField(max_length=50, blank=True, null=True)
    updated_at = models.DateTimeField()

    def __str__(self):
        return self.name