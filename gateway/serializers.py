from rest_framework import serializers
from gateway.models import GateWay


class GateWaySerializer(serializers.ModelSerializer):

    class Meta:
        model = GateWay
        fields = "__all__"
