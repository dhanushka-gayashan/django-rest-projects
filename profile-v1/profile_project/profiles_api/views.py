from rest_framework import viewsets, filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.settings import api_settings
from . import serializers
from . import models
from . import permissons


# Create your views here.
class UserLoginApiView(ObtainAuthToken):
    """ Handle creating user authentication tokens """
    """ Once user login, user will get a Token which needs to pass with other HTTP requests """

    # Add Default Rendering Class to enable View Users on Admin Interface and Browsable APIs
    # ObtainAuthToken does not have this class by default (ModelViewSet have this calls by default)
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class UserProfileViewSet(viewsets.ModelViewSet):
    """ Handle creating, reading and updating profiles """

    # User authentication
    authentication_classes = (TokenAuthentication,)

    # User can send HTTP GET / HEAD / OPTIONS Request (Read Only) without Authenticated
    # User need to be Authenticated to send HTTP POST / PATCH / PUT / DELETE  Request
    permission_classes = (permissons.UpdateOwnProfile,)

    # Serialize and Validate User Object
    serializer_class = serializers.UserProfileSerializer

    # Handle all DB operations. No need to override methods
    queryset = models.UserProfile.objects.all()

    # Filter and Search by Name or Email
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email')


class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """ Handle creating, reading and updating profile feed items """

    # User authentication
    authentication_classes = (TokenAuthentication,)

    # User can send HTTP GET / HEAD / OPTIONS Request (Read Only) without Authenticated
    # User need to be Authenticated to send HTTP POST / PATCH / PUT / DELETE  Request
    # permission_classes = (permissons.UpdateOwnStatus, IsAuthenticatedOrReadOnly)

    # User need to be Authenticated to send any kind of HTTP Request
    permission_classes = (permissons.UpdateOwnStatus, IsAuthenticated)

    # Serialize and Validate User Feed Item Object
    serializer_class = serializers.ProfileFeedItemSerializer

    # Handle all DB operations. No need to override methods
    queryset = models.ProfileFeedItem.objects.all()

    # Customize create() to set Authenticated User into 'user_profile' field ('user_profile' is a read-only field)
    # This allow to limit that Authenticated User only able to create Feed Items of his own profile
    def perform_create(self, serializer):
        """ Sets the user profile to the logged in user """

        # After 'Serializer' validate the Object, 'Serializer' call 'save()' to save object into DB
        # Therefore, we need to customize this behaviour to set Authenticated User as the 'user_profile'
        serializer.save(user_profile=self.request.user)






