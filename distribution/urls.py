from django.urls import path
from rest_framework import routers

from distribution.views.dsp import DistributionViewSet
from distribution.views.health import HealthCheck
from distribution.views.user import UserViewset

router = routers.SimpleRouter()
router.register(r"users", UserViewset)
router.register(r"dsps", DistributionViewSet)

urlpatterns = [
    path("health/", HealthCheck.as_view()),
]

urlpatterns += router.urls
