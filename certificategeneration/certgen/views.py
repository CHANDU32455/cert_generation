from django.shortcuts import render
from . models import *
from .serializer import CertificateSerializer, BulkCertificateSerializer
from rest_framework import viewsets

def index(request):
    return render(request, 'index.html')

def certgen(request):
    return render(request, 'index.html') 

def formresults(request):
    return render(request, 'index.html')


class CertificateView(viewsets.ModelViewSet):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer

class BulkCertificateView(viewsets.ModelViewSet):
    queryset = BulkCertificates.objects.all()
    serializer_class = BulkCertificateSerializer