from django.contrib.auth.models import User
from rest_framework import fields, serializers
from rest_framework.validators import UniqueValidator


class UserSerializer(serializers.ModelSerializer):
    username = fields.CharField(required=True, validators=[UniqueValidator(queryset=User.objects.all())])
    password = fields.CharField(write_only=True)
    is_active = fields.BooleanField(default=True)
    date_joined = fields.CharField(read_only=True)

    class Meta:
        fields = ("id", "username", "password", "is_active", "date_joined")
        model = User
