from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_401_UNAUTHORIZED

from owners.serializers import OwnerLoginSerializer


@api_view(['POST'])
def login(request):
    login_serializer = OwnerLoginSerializer(data=request.data)
    login_serializer.is_valid(raise_exception=True)
    username = login_serializer.validated_data['username']
    
    def get_user():
        try:
            return User.objects.get(username=username)
        except User.DoesNotExist:
            pass
        try:
            return User.objects.get(email=username)
        except User.DoesNotExist:
            pass
    
    user = get_user()

    if not user:
        return Response(status=HTTP_401_UNAUTHORIZED)

    if user.check_password(login_serializer.validated_data['password']):
        return Response({'token': user.auth_token.key, 'owner_id': user.owner.id})
    else:
        return Response(status=HTTP_401_UNAUTHORIZED)
