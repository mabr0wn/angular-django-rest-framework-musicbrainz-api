# Django
from django.urls import path, include
# Django rest
from rest_framework.schemas import get_schema_view
from rest_framework import routers
# Local
from albums.views import AlbumViewSet, RecordViewSet
from experiments import views

"""
Create a router and register our viewsets with it.
DefaultRouter() automatically created the api_root
from views, no longer required.
"""
router = routers.SimpleRouter()
router.register(r'experiments', views.ExperimentViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'album', AlbumViewSet)
router.register(r'records', RecordViewSet)

schema_view = get_schema_view(title='Pastebin API')

"""
The API URLs are now determined automatically by the router.
Additionally, we include the login URLs for the browsable API.
"""
urlpatterns = [
	# angular view
	path(r'', views.Index.as_view(), name='index'),
	# api
	path(r'api/', include(router.urls)),
	path(r'api-auth/', include('rest_framework.urls', namespace='rest_framework')),
	path(r'schema/', schema_view)
]
