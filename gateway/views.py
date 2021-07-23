from rest_framework import views, viewsets
from rest_framework.response import Response
from django.shortcuts import HttpResponse
from gettingstarted.config import APIResponse
from . import models
from . import serializers


class GateWayViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.GateWaySerializer

    def get_queryset(self):
        return models.GateWay.objects.all()
