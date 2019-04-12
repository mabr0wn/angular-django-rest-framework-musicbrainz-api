# Django
from django.urls import path, include
# Django rest
from rest_framework import routers
# Local
from auth import views

"""
Create a router and register our viewsets with it.
DefaultRouter() automatically created the api_root
from views, no longer required.
"""
router = routers.SimpleRouter()
router.register(r'users', views.UserViewSet)


"""
The API URLs are now determined automatically by the router.
Additionally, we include the login URLs for the browsable API.
"""
urlpatterns = [
	# api
    path(r'api/', include(router.urls)),
	path(r'api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]