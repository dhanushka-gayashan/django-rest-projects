from rest_framework import permissions


# This allow to limit that Authenticated User only able to update his own profile
class UpdateOwnProfile(permissions.BasePermission):
    """ Allow user to edit only their own profile """

    def has_object_permission(self, request, view, obj):
        """ Check user is trying to edit their own profile """

        # User can perform HTTP GET / HEAD / OPTIONS on all Profiles
        if request.method in permissions.SAFE_METHODS:
            return True

        # 'obj' is a 'User Profile Object'
        # User can only perform HTTP POST / PATCH / PUT / DELETE on User Profile
        # only if that 'obj' is his own User Profile
        return obj.id == request.user.id


# This allow to limit that Authenticated User only able to update Feed Items of his own profile
class UpdateOwnStatus(permissions.BasePermission):
    """ Allow user to update their own status """

    def has_object_permission(self, request, view, obj):
        """ Check the user is trying to update their own status """

        # User can perform HTTP GET / HEAD / OPTIONS on all Feed Items
        if request.method in permissions.SAFE_METHODS:
            return True

        # 'obj.user_profile' is a 'User Profile Object'
        # User can only perform HTTP POST / PATCH / PUT / DELETE on Feed Item
        # only if that 'obj.user_profile' is his own User Profile
        return obj.user_profile.id == request.user.id
