from django.conf.urls import url, include
from experiments import views
from rest_framework.routers import DefaultRouter

"""
Create a router and register our viewsets with it.
DefaultRouter() automatically created the api_root
from views, no longer required.
"""
router = routers.SimpleRouter()
router.register(r'experiments', views.ExerimentsViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'musicians', views.MusicianViewSet)
router.register(r'collections', CollectionViewSet)
router.register(r'records', RecordViewSet)

"""
The API URLs are now determined automatically by the router.
Additionally, we include the login URLs for the browsable API.
"""
urlpatterns = [
	url(r'^', include(router.urls)),
	url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
