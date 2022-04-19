from rest_framework.routers import SimpleRouter

from tickets.views import CouponsViewSet

app_name = 'tickets'

router = SimpleRouter()

router.register('', CouponsViewSet, basename='tickets')

urlpatterns = router.urls
