from rest_framework.routers import SimpleRouter

from restaurants.views import ResturantsViewSet

app_name = 'restaurants'

router = SimpleRouter()

router.register('', ResturantsViewSet, basename='restaurants')

urlpatterns = router.urls
