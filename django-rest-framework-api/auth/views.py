from django.shortcuts import render
from auth.serializers import UserSerializer
from django.contrib.auth.models import User


# Create your views here.

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This Viewset automatically provides 'list' and 'detail' actions
    using the ReadOnly model we know this will provide reas-only
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer