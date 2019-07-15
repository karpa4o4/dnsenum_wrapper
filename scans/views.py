from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets

from .models import Scan
from .serializers import ScanSerializer
from .tasks import start_domain_scan

class ScanViewSet(viewsets.ViewSet):
    @action(detail=False, methods=['post'])
    def start_scan(self, request):
        if 'domain' in request.POST and request.POST['domain']:
            scan = Scan.objects.create()
            start_domain_scan.delay(scan.id, request.POST['domain'])
            serializer = ScanSerializer(scan)
            return Response({'scan_id': serializer.data['id']})
        return Response(status=452)

    @action(detail=True, methods=['get'])
    def get_status(self, request, pk=None):
        scan = get_object_or_404(Scan, id=pk)
        serializer = ScanSerializer(scan)
        return Response({'scan_status': serializer.data['status']})

    @action(detail=True, methods=['get'])
    def get_result(self, request, pk=None):
        scan = get_object_or_404(Scan, id=pk)
        serializer = ScanSerializer(scan)
        return Response({'scan_result': '' if serializer.data['result'] is None else serializer.data['result'] })