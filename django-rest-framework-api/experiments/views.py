from experiments.models import Experiment, Musician
from experiments.permissions import IsOwnerOrReadOnly
from experiments.serializers import ExperimentSerializer, UserSerializer
from rest_framework import mixins
from rest_framework import generics
from rest_framework import permissions
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import renderers, viewsets, mixins
from django.contrib.auth.models import User

from django.shortcuts import render_to_response

import musicbrainzngs as mb

mb.set_useragent('PUT_EMAIL_HERE', version='0.0.1')

from django.shortcuts import render

def index(request):
    return render(request, 'musicians/index.html')

# def index(request):
#     context = {'musicians': []}
    
#     if request.GET.keys():
#         musician_queryset = Musician.objects.all()
        
#         if request.GET.get('genre'):
#             musician_queryset = musician_queryset.filter(genre=request.GET['genre'])
            
#         artist_kwarg = request.GET.get('artist', None)
#         if artist_kwarg:
#             musicians_queryset = musician_queryset.filter(artist=artist_kwarg)
            
#         context['musicians'] = musician_queryset
        
#         if context['musicians'].count() == 0 and artist_kwarg:
#             context['musicians'] = Musician.get_artist_tracks_from_musicbrainz_api(artist_kwarg)
    
#     return render_to_response('musicians/index.html', context)

def musician_detail(request, collection, record, artist):
    context = {
        'musician': Musician.objects.get(slug=artist, record__slug=record, record__collection__slug=collection)
    }
    
    return render_to_response('musicians/musician_detail.html', context)

# class MusicianViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin, mixins.RetrieveModelMixin):
#     queryset = Musician.objects.all()
#     serializer_class = MusicianSerializer

# """
# We can now group all three views classes into one now using
# the ViewSet class.
# """
class ExperimentViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides 'list', 'create', 'retrieve',
    'update', and 'destroy' actions.
    
    additionally we also provide an extra 'highlight' action
    """
    queryset = Experiment.objects.all()
    serializer_class = ExperimentSerializer
    # permission_classes = (permissions.IsOwnerOrReadOnly,)
    """
    Notice that we've also used the @detail_route decorator to create a custom action, 
    named highlight. This decorator can be used to add any custom endpoints that don't fit 
    into the standard create/update/delete style.
    
    Custom actions which use the @detail_route decorator will respond to GET requests by 
    default. We can use the methods argument if we wanted an action that responded to POST 
    requests.
    """
    @detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        experiment = self.get_object()
        return Response(experiment.highlighted)
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        
class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This Viewset automatically provides 'list' and 'detail' actions
    using the ReadOnly model we know this will provide reas-only
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
