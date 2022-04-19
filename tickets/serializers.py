from rest_framework import serializers

from tickets.models import Coupon

class CouponSerializer(serializers.ModelSerializer):
    restaurant_name = serializers.CharField(source='restaurant.name')

    class Meta:
        model = Coupon
        fields = ['id', 'name', 'max_purchase_count', 'available_coupons', 'restaurant_name']
