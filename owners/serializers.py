from rest_framework import serializers

class OwnerLoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=False)
    username = serializers.CharField(required=False)
    password = serializers.CharField(required=True)

    def validate(self, data):
        if not data.get('username') and not data.get('email'):
            raise serializers.ValidationError('You must provide either username or email')
        return data
