from django.shortcuts import render
from .models import Version, OVPNFile
from rest_framework import generics
from .serializers import VersionSerializer, OVPNFileSerializer


class VersionList(generics.ListCreateAPIView):
    queryset = Version.objects.all()
    serializer_class = VersionSerializer


class VersionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Version.objects.all()
    serializer_class = VersionSerializer


class OVPNFileList(generics.ListCreateAPIView):
    queryset = OVPNFile.objects.all()
    serializer_class = OVPNFileSerializer


class OVPNFileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = OVPNFile.objects.all()
    serializer_class = OVPNFileSerializer
