from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from restaurants.models import Restaurant
from restaurants.serializers import RestaurantSerializer


class ResturantsViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user.owner)
