from rest_framework import permissions, viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.reverse import reverse

from guardian.models import UserObjectPermission

from django.contrib.auth.models import User, Group
from .models import Post
from .serializers import UserSerializer, PostSerializer
from .permissions import UserModelPermission


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def api_root(request, format=None):
    return Response({
        'users': reverse('myapp:user-list', request=request, format=format),
        'countries': reverse('myapp:country-list', request=request, format=format)
    })


class UserViewSet(viewsets.ModelViewSet):
    """This viewset automatically provides `list` and `detail` actions."""
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [UserModelPermission]

    def perform_create(self, serializer):
        user = serializer.save()
        group_view = Group.objects.filter(name='viewers').get()
        group_add = Group.objects.filter(name='posters').get()
        group_edit = Group.objects.filter(name='editors').get()  # change and delete permission
        user.groups.add(group_view, group_add, group_edit)

    def perform_update(self, serializer):
        """special treatement for password, on PUT/PATCH"""
        if 'password' in serializer.validated_data:
            new_password = serializer.validated_data.pop('password')
            user = serializer.instance
            user.set_password(new_password)
        serializer.save()


class PostViewSet(viewsets.ModelViewSet):
    """This viewset automatically provides `list` and `detail` actions."""
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        obj = serializer.save(creator=self.request.user)
        UserObjectPermission.objects.assign_perm('change_post', self.request.user, obj=obj)
        UserObjectPermission.objects.assign_perm('delete_post', self.request.user, obj=obj)
