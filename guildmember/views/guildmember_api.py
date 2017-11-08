from django.shortcuts import get_object_or_404

from rest_framework import generics
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.response import Response

from .. import models
from .. import serializers

class MemberViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):
    queryset = models.Member.objects.all()
    serializer_class = serializers.MemberSerializer

class WeaponsummonViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):
    queryset = models.Weaponsummon.objects.all()
    serializer_class = serializers.WeaponsummonSerializer

class PowerViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):
    queryset = models.Power.objects.all()
    serializer_class = serializers.PowerSerializer

class PoolViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):
    queryset = models.Pool.objects.all()
    serializer_class = serializers.PoolSerializer

    # @detail_route(methods=['get'])
    # def members(self, request, pk, format=None):
    #     pool = self.get_object()
    #     print (dir(pool))
    #     member = pool.member
    #     serializer = serializers.MemberSerializer(member, many=True)
    #     return Response(serializer.data)
