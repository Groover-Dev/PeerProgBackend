from rest_framework.viewsets import ReadOnlyModelViewSet

from distribution.models.dsp import DSP
from distribution.serializers.dsp import DSPSerializer


class DistributionViewSet(ReadOnlyModelViewSet):
    queryset = DSP.objects.all()
    serializer_class = DSPSerializer
