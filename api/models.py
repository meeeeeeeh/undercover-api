from django.db import models


class Version(models.Model):
    version = models.CharField(max_length=30)


class OVPNFile(models.Model):
    file_name = models.CharField(max_length=100)
    file_version = models.IntegerField(default=0)
    file_settings = models.TextField(max_length=10000)


class Secret(models.Model):
    secret = models.CharField(max_length=255)
