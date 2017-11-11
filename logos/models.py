from django.db import models


# Create your models here.
class LogoAnalyze (models.Model):
    suggested_logo_name = models.CharField(max_length=200, default="Unknown")
    video = models.FileField(upload_to='videos', default="")
    precision = models.CharField(max_length=20, default="0.0")