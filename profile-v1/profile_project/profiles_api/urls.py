from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


# No need to define 'base_name' for this router, because Django REST get 'base_name' from 'queryset' in view
router = DefaultRouter()
router.register('profile', views.UserProfileViewSet)
router.register('feed', views.UserProfileFeedViewSet)

urlpatterns = [
    path('login/', views.UserLoginApiView.as_view()),
    path('', include(router.urls)),
]

