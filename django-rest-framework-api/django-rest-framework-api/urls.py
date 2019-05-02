"""django-rest-framework-api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
# Django
from django.urls import include, path, re_path
from django.contrib import admin
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.views.generic import TemplateView
from django.conf.urls.static import static
# Graphene for GraphQL
from graphene_django.views import GraphQLView
from .schema import schema
# Django rest framework
from rest_framework import routers
# Views
from artists.views import ArtistViewSet, AlbumViewSet, TrackViewSet
# Router
router = routers.SimpleRouter()
router.register(r'artists', ArtistViewSet)
router.register(r'albums', AlbumViewSet)
router.register(r'tracks', TrackViewSet)


urlpatterns = [
    path(r'admin/', admin.site.urls),
    path(r'api/', include(router.urls)),
    path(r'api-auth/', include('rest_framework.urls')),
    # angular view
    re_path('.*', TemplateView.as_view(template_name='index.html')),
    # graphql
    path(r'graphql/', csrf_exempt(GraphQLView.as_view(graphiql=True, schema=schema))),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

