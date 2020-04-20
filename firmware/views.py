from django.http import HttpResponse
from rest_framework import generics
from .models import *


class ServerUpdate(generics.ListAPIView):
    def get(self, request, *args, **kwargs):
        version = kwargs.get('buildVersion')

        last_version = ServerFirmware.objects.latest('buildVersion')
        if last_version:
            if version < last_version.buildVersion:
                firmaware_file = last_version.file
                response = HttpResponse(firmaware_file, content_type='application/octet-stream')
                response['Content-Disposition'] = f'inline; filename={last_version.nameVersion}.bin'
                return response
            else:
                return HttpResponse(status=200)
        return HttpResponse(status=204)


class ServerCheck(generics.ListAPIView):
    def get(self, request, *args, **kwargs):
        version = kwargs.get('buildVersion')

        last_version = ServerFirmware.objects.latest('buildVersion')
        if last_version:
            if version < last_version.buildVersion:
                return HttpResponse(status=200)
            else:
                return HttpResponse(status=202)
        return HttpResponse(status=204)


class EncoderUpdate(generics.ListAPIView):
    def get(self, request, *args, **kwargs):
        version = kwargs.get('buildVersion')

        last_version = EncoderFirmware.objects.latest('buildVersion')
        if last_version:
            if version < last_version.buildVersion:
                firmaware_file = last_version.file
                response = HttpResponse(firmaware_file, content_type='application/octet-stream')
                response['Content-Disposition'] = f'inline; filename={last_version.nameVersion}.bin'
                return response
            else:
                return HttpResponse(status=200)
        return HttpResponse(status=204)


class EncoderCheck(generics.ListAPIView):
    def get(self, request, *args, **kwargs):
        version = kwargs.get('buildVersion')

        last_version = EncoderFirmware.objects.latest('buildVersion')
        if last_version:
            if version < last_version.buildVersion:
                return HttpResponse(status=200)
            else:
                return HttpResponse(status=202)
        return HttpResponse(status=204)
