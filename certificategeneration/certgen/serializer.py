from rest_framework import serializers
from certgen.models import Certificate, BulkCertificates

class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = '__all__'

class BulkCertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = BulkCertificates
        fields = '__all__'