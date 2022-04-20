from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from tickets.models import Coupon
from tickets.serializers import CouponSerializer


class CouponsViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Coupon.objects.all()
    serializer_class = CouponSerializer

    def get_queryset(self):
        return self.queryset.filter(restaurant__owner=self.request.user.owner)


    @action(detail=False, methods=['get'])
    def restaurant_coupons(self, request):
        restaurant_id = self.request.query_params.get('restaurant')
        qs = self.queryset.filter(restaurant_id=restaurant_id)
        data = self.serializer_class(qs, many=True)
        return Response(data.data)
