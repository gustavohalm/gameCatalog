from rest_framework import routers
from .views import CategoryViewSet, PublisherViewSet, GameViewSet


router = routers.DefaultRouter()

router.register('category', CategoryViewSet)
router.register('publisher', PublisherViewSet)
router.register('game', GameViewSet)

urlpatterns = router.urls
