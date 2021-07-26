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


class Test(views.APIView):

    def get(self, *args, **kwargs):
        data = [
            {
                'id': '000000001',
                'avatar': 'https://gw.alipayobjects.com/zos/rmsportal/ThXAXghbEsBCCSDihZxY.png',
                'title': '你收到了 14 份新周报',
                'datetime': '2017-08-09',
                'type': 'notification',
            },
        ]

        return Response({'data':data})
