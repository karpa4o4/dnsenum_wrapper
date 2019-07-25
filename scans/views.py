from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import RetrieveAPIView

from .models import Scan
from .serializers import ScanStartSerializer, ScanGetStatusSerializer, ScanGetResultSerializer
from .tasks import start_domain_scan

class ScanStartView(APIView):
    def post(self, request):
        if 'domain' in request.POST:
            scan = Scan.objects.create()
            start_domain_scan.delay(scan.id, request.POST['domain'])
            serializer = ScanStartSerializer(scan)
            return Response(serializer.data)
        return Response(status=452)

class ScanGetStatusView(RetrieveAPIView):
    queryset = Scan.objects.all()
    serializer_class = ScanGetStatusSerializer

class ScanGetResultView(RetrieveAPIView):
    queryset = Scan.objects.all()
    serializer_class = ScanGetResultSerializer