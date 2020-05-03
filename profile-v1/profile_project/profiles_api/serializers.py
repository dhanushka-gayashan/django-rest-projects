from rest_framework import serializers
from . import models


class UserProfileSerializer(serializers.ModelSerializer):
    """ Serializes a user profile object """

    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')

        # Access password field is allow only for writing operations
        # In create/update Form, password field showing as "password type field"
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }

    def create(self, validated_data):
        """ Create and return a new user """
        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )

        return user

    # Fixing a bug in Django REST Framework - Hashing the password when update the given instance
    def update(self, instance, validated_data):
        """Handle updating user account"""
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)

        return super().update(instance, validated_data)


class ProfileFeedItemSerializer(serializers.ModelSerializer):
    """ Serializes a profile feed item object """

    class Meta:
        model = models.ProfileFeedItem
        fields = ('id', 'user_profile', 'status_text', 'created_on')

        # Authenticated User should only able to create Feed Items for his own profile.
        # Therefore, we need to make 'user_profile' field as a 'read-only' field
        # Then, Authenticated User cannot select other profiles when create a new Feed Item
        extra_kwargs = {
            'user_profile': {'read_only': True},
        }




