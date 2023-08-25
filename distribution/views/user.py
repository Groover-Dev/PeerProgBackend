from django.contrib.auth.models import User
from rest_framework import permissions, viewsets

from distribution.serializers import UserSerializer


class UserViewset(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    queryset = User.objects.all()
    serializer_class = UserSerializer
