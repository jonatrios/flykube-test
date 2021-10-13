from rest_framework.routers import DefaultRouter
from apps.travels.views import TravelGenericViewSet


router = DefaultRouter()

router.register(r'travels', TravelGenericViewSet, basename='travel_view_set')

urlpatterns = router.urls