# Generated by Django 4.0.4 on 2022-04-19 04:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('restaurants', '0001_initial'),
        ('guests', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('max_purchase_count', models.PositiveIntegerField(verbose_name='How many of this coupons we can purchase')),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='coupons', to='restaurants.restaurant')),
            ],
        ),
        migrations.CreateModel(
            name='CouponPurchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coupon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='purchases', to='tickets.coupon')),
                ('guest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='coupons', to='guests.guest')),
            ],
        ),
    ]
