

from .serializers import UserSerializer,SennaSerializer
from django.contrib.auth.models import User
from front.models import Senna
from rest_framework import routers, serializers, viewsets



from django.contrib.auth.models import User
# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class SennaViewSet(viewsets.ModelViewSet):
    queryset = Senna.objects.all()
    serializer_class = SennaSerializer