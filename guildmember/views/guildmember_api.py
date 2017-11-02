from rest_framework import generics

from .. import models
from .. import serializers


class ListCreateMember(generics.ListCreateAPIView):
    queryset = models.Member.objects.all()
    serializer_class = serializers.MemberSerializer

class RetrieveUpdateDestroyMember(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Member.objects.all()
    serializer_class = serializers.MemberSerializer

class ListCreatePool(generics.ListCreateAPIView):
    queryset = models.Pool.objects.all()
    serializer_class = serializers.PoolSerializer

class RetrieveUpdateDestroyPool(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Pool.objects.all()
    serializer_class = serializers.PoolSerializer
