from rest_framework import serializers

class OwnerLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

    # def validate(self, data):
    #     if not data.get('username') and not data.get('email'):
    #         raise serializers.ValidationError('You must provide either username or email')
    #     return data
