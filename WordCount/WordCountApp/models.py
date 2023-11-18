from django.db import models


class Text(models.Model):
    text = models.FileField(upload_to='uploads/')
