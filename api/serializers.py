from rest_framework import serializers
from .models import Version, OVPNFile


class VersionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Version
        fields = ['version']


class OVPNFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = OVPNFile
        fields = ['id',
                  'file_name',
                  'file_version',
                  'client',
                  'dev',
                  'proto',
                  'remote',
                  'resolv_retry',
                  'nobind',
                  'persist_key',
                  'persist_tun',
                  'remote_sert_tls',
                  'auth',
                  'cipher',
                  'ignore_unknown_option',
                  'block_outside_dns',
                  'verb']
