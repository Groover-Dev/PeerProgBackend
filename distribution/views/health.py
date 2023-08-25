from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView


class HealthCheck(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, *args, **kwargs):
        return Response({"status": "ok"}, 200)
