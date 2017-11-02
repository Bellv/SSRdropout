from rest_framework import serializers

from . import models

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Member
        fields = ('__all__')

class PoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Pool
        fields = ('__all__')
