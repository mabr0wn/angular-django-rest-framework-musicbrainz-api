from django.conf.urls import url, include
from experiments import views
from rest_framework.schemas import get_schema_view

from rest_framework import routers

from assortments.views import CollectionViewSet, RecordViewSet
from experiments.views import MusicianViewSet

"""
Create a router and register our viewsets with it.
DefaultRouter() automatically created the api_root
from views, no longer required.
"""
router = routers.SimpleRouter()
router.register(r'experiments', views.ExerimentsViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'musicians', MusicianViewSet)
router.register(r'assortment', CollectionViewSet)
router.register(r'records', RecordViewSet)

schema_view = get_schema_view(title='Pastebin API')

"""
The API URLs are now determined automatically by the router.
Additionally, we include the login URLs for the browsable API.
"""
urlpatterns = [
	url(r'^api/', include(router.urls)),
	url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
	url(r'^schema/$', schema_view),
	
	url(r'^recordings/(?P<album>[\w-]+)/(?P<track>[\w-]+)/(?P<artist>[\w-]+)/$',
    	views.musician_detail, name='musician_detail_view'),
	url(r'^$', views.index),
]
