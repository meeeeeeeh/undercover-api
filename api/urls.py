from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *

app_name = 'api'

urlpatterns = [
    path('version/<str:secret>', VersionList.as_view()),
    path('vpn_files/<str:secret>', OVPNFileList.as_view()),
    path('vpn_files/<str:file_name>/<str:secret>', OVPNFileDetail.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
