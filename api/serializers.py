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
                  'file_settings']
