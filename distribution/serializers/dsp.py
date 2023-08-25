from rest_framework import serializers

from distribution.models.dsp import DSP


class DSPSerializer(serializers.ModelSerializer):
    class Meta:
        model = DSP
        fields = ("id", "name")
