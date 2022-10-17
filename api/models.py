from django.db import models


class Version(models.Model):
    version = models.CharField(max_length=30)


class OVPNFile(models.Model):
    file_name = models.CharField(max_length=100)
    file_version = models.IntegerField(default=0)
    client = models.BooleanField(default=True)
    dev = models.CharField(max_length=3)
    proto = models.CharField(max_length=4)
    remote = models.CharField(max_length=30)
    resolv_retry = models.CharField(max_length=10)
    nobind = models.BooleanField(default=True)
    persist_key = models.BooleanField(default=True)
    persist_tun = models.BooleanField(default=True)
    remote_sert_tls = models.CharField(max_length=10)
    auth = models.CharField(max_length=10)
    cipher = models.CharField(max_length=30)
    ignore_unknown_option = models.CharField(max_length=40)
    block_outside_dns = models.BooleanField(default=True)
    verb = models.IntegerField()
