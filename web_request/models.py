from django.db import models


class WebRequest(models.Model):
    host = models.CharField(max_length=500)
    path = models.TextField()
    method = models.CharField(max_length=6)
    get_data = models.TextField(blank=True, null=True)
    post_data = models.TextField(blank=True, null=True)
    uri = models.TextField()
