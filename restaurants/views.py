from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from restaurants.models import Restaurant
from restaurants.serializers import RestaurantSerializer


class ResturantsViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user.owner)
    

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        restaurant = Restaurant.objects.create(
            owner=self.request.user.owner, name=serializer.validated_data['name'])
        return Response({'id': restaurant.id, 'name': restaurant.name})
        
