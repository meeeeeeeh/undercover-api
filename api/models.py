from django.db import models


class Version(models.Model):
    version = models.CharField(max_length=30)

    def __str__(self):
        return self.version


class OVPNFile(models.Model):
    file_name = models.CharField(max_length=100, unique=True)
    file_version = models.IntegerField(default=0)
    file_settings = models.TextField(max_length=10000)

    def __str__(self):
        return self.file_name


class Secret(models.Model):
    secret = models.CharField(max_length=255)

    def __str__(self):
        return self.secret
