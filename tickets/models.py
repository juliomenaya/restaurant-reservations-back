from django.db import models
from restaurants.models import Restaurant
from guests.models import Guest

# Create your models here.
class Coupon(models.Model):
    restaurant = models.ForeignKey(Restaurant, related_name='coupons', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    max_purchase_count = models.PositiveIntegerField(
        verbose_name='How many of this coupons we can purchase',
    )

    @property
    def available_coupons(self):
        return self.max_purchase_count - self.purchases.count()



class CouponPurchase(models.Model):
    coupon = models.ForeignKey(Coupon, related_name='purchases', on_delete=models.CASCADE)
    guest = models.ForeignKey(Guest, related_name='coupons', on_delete=models.CASCADE)
