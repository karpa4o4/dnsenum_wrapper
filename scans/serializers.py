from rest_framework.serializers import ModelSerializer

from .models import Scan

class ScanStartSerializer(ModelSerializer):
    class Meta:
        model = Scan
        fields = ('id',)

class ScanGetResultSerializer(ModelSerializer):
    class Meta:
        model = Scan
        fields = ('result',)

class ScanGetStatusSerializer(ModelSerializer):
    class Meta:
        model = Scan
        fields = ('status',)