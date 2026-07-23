from rest_framework import serializers
from django.contrib.auth import authenticate
from accounts.models import User, Invite
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class RegisterSerializer(serializers.ModelSerializer):
    password_confirm = serializers.CharField(write_only=True)
    invite_code = serializers.CharField(write_only=True, max_length=4)

    class Meta:
        model = User
        fields = ['username', 'password', 'password_confirm', 'invite_code']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate_invite_code(self, value):
        if not Invite.objects.filter(code=value, is_active=True).exists():
            raise serializers.ValidationError("Code is invalid")
        return value

    def validate(self, attrs):
        if attrs['password'] != attrs['password_confirm']:
            raise serializers.ValidationError({"password_confirm": "Passwords does not match"})
        return attrs

    def create(self, validated_data):
        validated_data.pop('password_confirm')
        invite_code = validated_data.pop('invite_code')

        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
        )

        Invite.objects.filter(code=invite_code).update(is_active=False)
        return user
    
class LogInSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token["username"] = user.username
        return token
    
class InviteCheckSerializer(serializers.Serializer):
    invite_code = serializers.CharField(max_length=4)

    def validate_invite_code(self, value):
        if not Invite.objects.filter(code=value, is_active=True).exists():
            raise serializers.ValidationError("Invitation code is invalid")
        return value
