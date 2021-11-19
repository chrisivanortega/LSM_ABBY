from rest_framework import routers, serializers, viewsets
from django.contrib.auth.models import User
from front.models import Senna

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

class SennaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Senna
        fields = ['id', 'name', 'img', 'desc']