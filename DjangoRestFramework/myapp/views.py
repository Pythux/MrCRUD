from rest_framework import permissions, viewsets
from rest_framework.decorators import api_view, permission_classes, action
from rest_framework.response import Response
from rest_framework.reverse import reverse

from django.contrib.auth.models import User
from .models import Country
from .serializers import UserSerializer, CountrySerializer, NicePlaceSerializer
# from .permissions import IsOwnerOrReadOnly


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def api_root(request, format=None):
    return Response({
        'users': reverse('myapp:user-list', request=request, format=format),
        'countries': reverse('myapp:country-list', request=request, format=format)
    })


class UserViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    # permission_classes = [IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        """overide instance save"""
        # can give others fields, the "owner" field here
        serializer.save(owner=self.request.user)

    @action(detail=True)
    def places(self, request, *args, **kwargs):
        """provide an extra action "places",
            actions are "list, create, retrieve, update, partial_update, ..."
        """
        country = self.get_object()
        niceplace = NicePlaceSerializer(country.niceplace_set.all(), many=True)
        return Response(niceplace.data)
