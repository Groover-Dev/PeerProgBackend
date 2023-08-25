from django.db import models


class DSP(models.Model):
    name = models.CharField(max_length=30, null=False, blank=False, unique=True)
