from owners.models import Owner
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from restaurants.models import Restaurant
from tickets.models import Coupon, CouponPurchase
from guests.models import Guest
from django.db import transaction



def create_owner(username, first_name, last_name, email, password):
    user = User.objects.create_user(
        username=username, first_name=first_name, last_name=last_name, email=email, password=password
    )
    token1 = Token.objects.create(user=user)
    owner1 = Owner.objects.create(user=user)
    return owner1


def create_restaurant(owner, name):
    return Restaurant.objects.create(owner=owner, name=name)


def create_coupon(restaurant, name, max_purchase_count):
    return Coupon.objects.create(
        restaurant=restaurant, name=name, max_purchase_count=max_purchase_count)


def create_guest(name, lastname):
    return Guest.objects.create(name=name, lastname=lastname)


def create_coupon_purchase(coupon, guest):
    return CouponPurchase.objects.create(coupon=coupon, guest=guest)



def initial_load():
    with transaction.atomic():
        owner1 = create_owner('julio.mendez', 'Julio', 'Mendez',
            'juliomenaya@gmail.com', '12345678')

        for i in range(1, 6):
            create_restaurant(owner1, f'{owner1.user.first_name} number-{i}')
        
        for i, restaurant in enumerate(owner1.restaurants.all(), 1):
            create_coupon(restaurant, f'Coupon {i}', 20)
        
        guest1 = create_guest('Isa', 'Vargas')
        guest2 = create_guest('Miguel', 'Rubi')

        coupon1 = Coupon.objects.first()
        coupon2 = Coupon.objects.last()

        # first guest bought 2 coupons
        create_coupon_purchase(coupon1, guest1)
        create_coupon_purchase(coupon1, guest1)

        # second guest bought 1 coupon1 and 1 coupon2
        create_coupon_purchase(coupon1, guest2)
        create_coupon_purchase(coupon2, guest2)

        owner2 = create_owner('miguel.rubi', 'Miguel', 'Rubi',
                'miguel.rubi@gmail.com', '12345678')

        for i in range(1, 6):
            create_restaurant(owner2, f'{owner2.user.first_name} number-{i}')
        
        for i, restaurant in enumerate(owner2.restaurants.all(), 1):
            create_coupon(restaurant, f'Coupon {i}', 20)
