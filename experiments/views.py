from experiments.models import Experiment
from experiments.permissions import IsOwnerReadOnly
from experiments.serializers import ExperimentSerializer, UserSerializer
from rest_framework import mixins
from rest_framework import generics
from rest_framework import permissions
from rest_framework.decarators import api_view
from rest_framework.response import Response
from rest_framework import renderers

"""
This will create a reverse lookup for our users && experiments.
api_root your default, sends our request and the repsonse
will be users && experiments.
"""
@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'experiments': reverse('experiment-list', request=request, format=format)
    })

"""
Create an endpoint for experiment highlights, which is missing from our pastebin API,
we want this to display HTML not json unlike other API endpoints.  This type
of style is called pre-rendered HTML(StaticHTMLRendered).  What is happening here is
then render it to a pre-rendered HTML page.

def get is requesting data from experiment and return the data from experiment model class
with just the data we stated in field highlighted which is self.highlighted from
our def save() method.
"""

class ExperimentHighlight(generics.GenericAPIView):
  queryset = Experiment.objects.all()
  renderer_classes = (renderers.StaticHTMLRenderer,)
  
  def get(self, request, *args, **kwargs):
      experiment = self.get_object()
      return Response(experiment.highlighted) # returning code, lexer, formatter
    
"""
Here we are going to have a class ExperimentList that has mixins and generics.
Mixins are sort of a class that are used to "mix in" extra properties and methods
into a class.  This allows you to create classes in a combining style.
-- Mixins, small classes that add or augment a single feature, are an excellent
way to customize and modify your views.

Generic is a pre-built view that provides provide commonly uesd patterns, it saves you time.

We also are going to shorten this by using *args && **kwargs,
which simply *args will call th fields e.g. 'id', 'title', etc.
**kwargs will call the fields and assigned value to that field such as 'foo = \"bar\"\n"'
this is much less writing involved now instead of listing out to call the serialization data
for each method we only have to define in the class and by using *, ** Python will know.
"""

class ExperimentList(mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     generics.GenericAPIView):
    # Queryset is going to call all the objects in Experiment Model
    queryset = Experiment.objects.all()
    # call the fields from the serializer we made.
    serializer_class = ExperimentSerializer
    
    # IsAuthenticatedOrReadyOnly, which will ensure that authenticated requests get read-write access,
    # and unauthenticated requests get read-only access.
    permission_classes = (permission.IsAuthenticatedOrReadOnly, 
                          IsOwnerOrReadOnly,)
    
    
    """
    By calling the *, ** we have now made our code much more
    simple and easy to write as well as read.
    """
    def get(self, request, *args, **kwargs):
        # return the list of fields with its values.
        return self.list(request, *args, **kwargs)
     
    # return the newly created args and kwargs
    def post(self, request, *args, *kwargs):
        return self.create(request, *args, **kwargs)
    
    # allows a user to save a created change in our Experiment List,
    # from the data that has been serialized.
    # The create() method of our serializer will not be passed in
    # unless you are authenticated.
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

"""
We are building our view using GenericAPIView and adding in
ListModelMixin and CreateModelMixin.

The base class provides the core functionality, and the mixin classes
provide the .list() and .create() actions.  we're then explicity binding
the get and post methods to the appropriate actions.
"""

class ExperimentDetail(mixins.RetrieveModelMixin,
                       mixins.UpdateModelMixin,
                       mixins.DestroyModelMixin,
                       generics.GenericAPIView):
  queryset = Experiment.objects.all()
  serializer_class = ExperimentSerializer
  
  permission_classes = (permission.IsAuthenticatedOrReadOnly, 
                          IsOwnerOrReadOnly,)
    
  
  def get(self, request, *args, **kwargs):
      return self.retrieve(request, *args, **kwargs)
    
  def put(self, request, *args, **kwargs):
      return self.update(request, *args, **kwargs)
  
  def delete(self, request, *args, **kwargs):
      return self.destroy(request, *args, **kwargs)
    

"""
We will also add a couple of views to views.py We'd like to just use read-only views for the user
representation, so we will use the ListAPIView and RetreieveAPIView generic class-base views.
"""

from django.contrib.auth.models import User

class UserList(generics.ListAPIViews):
  queryset = User.objects.all()
  serializer_class = UserSerializer
  
class UserDetail(generics.RetreiveAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer
    
# from rest_framework import status
# from rest_framework.decarators import api_view
# from rest_framework.response import Response
# from experiments.models import Experiment
# from experiments.serializers import ExperimentSerializer


# """
# Going to rewrite this method since we do not need to use JSONResponse also it is very unsafe to exempt crsf
# use the @api_view decorators instead.

# @api_view decorator works with function based views.
# """

# @api_views(['GET', 'POST'])
# # allows GET and POST methods only.
# # Going to add format support suffixes to our API endpoints
# # Gives us URLs that explicity reder to a given format. and means our API will be able
# # to handle URLs such as 'http://example.com/api/items/4.json'
# def experiment_list(request, format=None):
#     """
#     List all code snippets, or create a new snippet
#     """
#     if request.method == 'GET':
#         # get all the experiment objects
#         experiments = Experiment.objects.all()
#         # call the fields(many=True)
#         serializer = ExperimentSerializer(experiments, many=True)
#         return Response(serializer.data)
    
#     elif request.method == 'POST':
#         # change from data=data to request.data
#         serializer = ExperimentSerializer(data=request.data)
#         if serializer.is_valid():
#             # save it with a 201 http status of created 
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         # error is not valid
#         return Repsonse(serializer.errors, status=status.HTTP._400_BAD_REQUEST)

# @api_view(['GET', 'PUT', 'DELETE'])
# def experiment_detail(request, pk, format=None):
#     """
#     Retrieve, update, or delete a code experiment
#     """
#     try:
#         experiment = Experiment.objects.get(pk=pk)
#     except Experiment.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
    
#     if request.method == 'GET':
#         serializer = ExperimentSerializer(experiment)
#         return Response(serializer.data)
    
#     elif request.method == 'PUT':
#         serializer = ExperimentSerializer(experiment, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     elif request.method == 'DELETE':
#         experiment.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

    
    
  
