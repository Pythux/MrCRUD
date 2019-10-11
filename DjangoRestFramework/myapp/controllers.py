from rest_framework import permissions, viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.reverse import reverse

from django.contrib.contenttypes.models import ContentType
from guardian.models import UserObjectPermission, GroupObjectPermission

from django.contrib.auth.models import Group
from .models import Post, MyUser, UserLottie
from .validators import UserSerializer, PostSerializer, LottieSerializer
from .permissions import PostNoAuthModelPermission, OwnerModifyModelPermission

from .controllers_mixins import AllowMixin


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def api_root(request, format=None):
    return Response({
        'users': reverse('myapp:user-list', request=request, format=format),
        'countries': reverse('myapp:country-list', request=request, format=format)
    })


class UserViewSet(AllowMixin, viewsets.ModelViewSet):
    """This viewset automatically provides `list` and `detail` actions."""
    queryset = MyUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [PostNoAuthModelPermission, OwnerModifyModelPermission]

    def perform_create(self, serializer):
        user = serializer.save()
        user.is_staff = True  # allow admin site
        user.save()
        user.groups.add(*[Group.objects.filter(name=name).get() for name in
                        ['viewers', 'posters', 'editors']])

    def perform_update(self, serializer):
        """special treatement for password, on PUT/PATCH"""
        if 'password' in serializer.validated_data:
            new_password = serializer.validated_data.pop('password')
            user = serializer.instance
            user.set_password(new_password)
        serializer.save()


class PostViewSet(AllowMixin, viewsets.ModelViewSet):
    """This viewset automatically provides `list` and `detail` actions."""
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        obj = serializer.save(creator=self.request.user)
        UserObjectPermission.objects.assign_perm('change_post', self.request.user, obj=obj)
        UserObjectPermission.objects.assign_perm('delete_post', self.request.user, obj=obj)

    def perform_destroy(self, instance):
        content_type = ContentType.objects.get_for_model(Post)
        UserObjectPermission.objects.filter(
            object_pk=instance.pk, content_type=content_type).delete()
        GroupObjectPermission.objects.filter(
            object_pk=instance.pk, content_type=content_type).delete()
        instance.delete()


class LottieViewSet(AllowMixin, viewsets.ModelViewSet):
    """store lottie file for user profile"""
    queryset = UserLottie.objects.all()
    serializer_class = LottieSerializer
    permission_classes = [permissions.IsAuthenticated, OwnerModifyModelPermission]
