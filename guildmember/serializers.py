from rest_framework import serializers

from . import models

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Member
        fields = (
            'name',
            'description',
            'gb_name',
            'gb_id',
            'gb_gender',
            'gb_class',
            'gb_waifu',
            'facebook',
            'twitter',
            'discord',
            'status'
        )
        

class PoolSerializer(serializers.ModelSerializer):
    # members = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = models.Pool
        fields = (
            # 'members',
            'star',
            'order'
        )
