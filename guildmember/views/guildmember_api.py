from django.shortcuts import get_object_or_404

from rest_framework import generics
from rest_framework import viewsets

from .. import models
from .. import serializers

class MemberViewSet(viewsets.ModelViewSet):
    queryset = models.Member.objects.all()
    serializer_class = serializers.MemberSerializer

class PoolViewSet(viewsets.ModelViewSet):
    queryset = models.Pool.objects.all()
    serializer_class = serializers.PoolSerializer

