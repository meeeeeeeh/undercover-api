from .models import Version, OVPNFile
from rest_framework import generics
from .serializers import VersionSerializer, OVPNFileSerializer
from .models import Secret
import hashlib
from rest_framework.response import Response
from rest_framework import status


class VersionList(generics.ListAPIView):
    queryset = Version.objects.all()
    serializer_class = VersionSerializer

    def get(self, request, secret):
        secret1 = Secret.objects.all()[0]
        encoded_secret1 = secret1.secret.encode()
        result_secret1 = hashlib.sha256(encoded_secret1).hexdigest()

        if secret == result_secret1:
            return self.list(request)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


class OVPNFileList(generics.ListAPIView):
    queryset = OVPNFile.objects.all()
    serializer_class = OVPNFileSerializer

    def get(self, request, secret):
        secret1 = Secret.objects.all()[0]
        encoded_secret1 = secret1.secret.encode()
        result_secret1 = hashlib.sha256(encoded_secret1).hexdigest()

        if secret == result_secret1:
            return self.list(request)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


class OVPNFileDetail(generics.RetrieveAPIView):
    queryset = OVPNFile.objects.all()
    serializer_class = OVPNFileSerializer
    lookup_field = 'file_name'

    def get(self, request, file_name, secret):
        secret1 = Secret.objects.all()[0]
        encoded_secret1 = secret1.secret.encode()
        result_secret1 = hashlib.sha256(encoded_secret1).hexdigest()

        if secret == result_secret1:
            return self.retrieve(request)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
