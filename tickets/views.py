from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from tickets.models import Coupon
from tickets.serializers import CouponSerializer


class CouponsViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Coupon.objects.all()
    serializer_class = CouponSerializer

    def get_queryset(self):
        return self.queryset.filter(restaurant__owner=self.request.user.owner)
