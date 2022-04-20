from rest_framework import serializers

from tickets.models import Coupon

class CouponListSerializer(serializers.ModelSerializer):
    restaurant_name = serializers.CharField(source='restaurant.name', read_only=True)

    class Meta:
        model = Coupon
        fields = ['id', 'name', 'max_purchase_count', 'available_coupons', 'restaurant_name']


class CouponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coupon
        fields = ["restaurant", "name", "max_purchase_count"]
