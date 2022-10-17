from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *

app_name = 'api'

urlpatterns = [
    path('versions/', VersionList.as_view()),
    path('versions/<int:pk>', VersionDetail.as_view()),
    path('vpn_files/', OVPNFileList.as_view()),
    path('vpn_files/<int:pk>', OVPNFileDetail.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
