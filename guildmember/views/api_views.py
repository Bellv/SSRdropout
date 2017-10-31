from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .. import models
from .. import serializers


class ListCreateMember(APIView):
    def get(self, request, format=None):
        members = models.Member.objects.all()
        serializer = serializers.MemberSerializer(members, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = serializers.MemberSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class ListCreatePool(APIView):
    def get(self, request, format=None):
        pools = models.Pool.objects.all()
        serializer = serializers.PoolSerializer(pools, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = serializers.PoolSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
