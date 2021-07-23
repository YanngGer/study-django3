from rest_framework import views, viewsets
from rest_framework.response import Response
from gettingstarted.config import APIResponse
from . import models
from . import serializers


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.UserSerializer

    def perform_destroy(self, instance):
        instance.delete()

    def get_queryset(self):
        return models.User.objects.all()


class CurrentUser(views.APIView):
    def get(self, *args, **kwargs):
        current_user = self.request.user
        if current_user:
            data = serializers.UserSerializer(current_user).data
            return APIResponse(data=data)
