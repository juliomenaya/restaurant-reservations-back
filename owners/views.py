from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_401_UNAUTHORIZED

from owners.serializers import OwnerLoginSerializer


@api_view(['POST'])
def login(request):
    login_serializer = OwnerLoginSerializer(data=request.data)
    login_serializer.is_valid(raise_exception=True)

    try:
        if username := login_serializer.validated_data.get('username'):
            user = User.objects.get(username=username)
        else:
            user = User.objects.get(email=login_serializer.validated_data.get('email'))
    except User.DoesNotExist:
        return Response(status=HTTP_401_UNAUTHORIZED)

    if user.check_password(login_serializer.validated_data['password']):
        return Response({'token': user.auth_token.key, 'owner_id': user.owner.id})
    else:
        return Response(status=HTTP_401_UNAUTHORIZED)
