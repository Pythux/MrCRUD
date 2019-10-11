from rest_framework import permissions
from rest_framework.permissions import DjangoModelPermissions, DjangoObjectPermissions


class OwnerModifyModelPermission(permissions.BasePermission):
    """Custom permission to only allow owners of an object to edit it."""

    def has_object_permission(self, request, view, obj):
        """permission for object"""
        if request.method in ('HEAD', 'OPTIONS', 'GET'):
            return True

        if request.method in ('DELETE', 'PATCH', 'PUT'):
            return obj == request.user
        return False


class PostNoAuthModelPermission(permissions.BasePermission):
    """Custom permission to only allow owners of an object to edit it."""

    def has_permission(self, request, view):
        """permission for list:"""
        if request.method in ('HEAD', 'OPTIONS'):
            return True
        if request.method == 'POST':
            return True
        if request.method == 'GET':
            if request.user and request.user.is_authenticated:
                return True

        if request.method in ('DELETE', 'PATCH', 'PUT'):
            """will be checked by object_permission"""
            return True
        return False


class DjangoModelPermissionsView(DjangoModelPermissions):
    """Permission that will be checked on list"""
    perms_map = DjangoModelPermissions.perms_map.copy()  # copy to avoid side effect
    perms_map['GET'] = ['%(app_label)s.view_%(model_name)s']


class DjangoObjectPermissionsView(DjangoObjectPermissions):
    """Permission that will be checked on detail"""
    perms_map = DjangoObjectPermissions.perms_map.copy()  # copy to avoid side effect
    perms_map['GET'] = ['%(app_label)s.view_%(model_name)s']


"""
DjangoModelPermissions and DjangoObjectPermissions:

DjangoObjectPermissions:
    look for (model + object) permission if it's on detail (GET/PATCH/PUT/DELETE)
    look for model permission if it's on list (GET/POST)

    object permission are weak pointer, they don't get deleted on object deletion
"""

# https://docs.djangoproject.com/en/2.2/topics/auth/default/#permissions-and-authorization

# A user in a group automatically has the permissions granted to that group
# myuser.groups.add(group, group, ...)
""" Model Permission:

from django.contrib.auth.models import Permission, User, Group
from django.contrib.contenttypes.models import ContentType

from myapp.models import Post

content_type = ContentType.objects.get_for_model(Post)
content_type.permission_set.all()
permission = content_type.permission_set.filter(codename='add_post').get()

#  Create a specific permition:
# permission = Permission.objects.create(
#     codename='add_post',
#     name='Can add post',
#     content_type=content_type,
# )

user = User.objects.get(username='john')
user.has_perm('myapp.add_post')
user.user_permissions.add(permission)

# regenerate cached permissions:
user = User.objects.get(username='john')

user.has_perm('myapp.add_post')
user.user_permissions.remove(permission)

# now, the Group:
# group_add = Group.objects.create(name='posters')
# group_view = Group.objects.create(name='viewers')

group_add = Group.objects.filter(name='posters').get()  # get an existing group
group_view = Group.objects.filter(name='viewers').get()  # get an existing group


permission_view = content_type.permission_set.filter(codename='view_post').get()
group_view.permissions.add(permission_view)

permission_add = content_type.permission_set.filter(codename='add_post').get()
group_add.permissions.add(permission_add)

user.user_permissions.all()
user.get_group_permissions()

user.groups.add(group_view, group_add)
user = User.objects.get(username='john')  # delete cached permission in user object
user.get_group_permissions()

Group.objects.filter(name='posters').get()
"""


""" Object Permission:
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from myapp.models import Post

post = Post.objects.filter(title='hi').get()

user = User.objects.get(username='john')

permission_view = content_type.permission_set.filter(codename='view_post').get()

user.has_perm('myapp.view_post', post)

from guardian.models import UserObjectPermission

#  Both work, refere to the codename of the permission inside the object.content_type
# UserObjectPermission.objects.assign_perm(permission_view, user, obj=post)
UserObjectPermission.objects.assign_perm('view_post', user, obj=post)

# Both work, because we have the object
user.has_perm('myapp.view_post', post)
user.has_perm('view_post', post)

from guardian.shortcuts import remove_perm

# remove_perm('myapp.view_post', user, post)
remove_perm('view_post', user, post)

# user = User.objects.get(username='john') # not cached
user.has_perm('myapp.view_post', post)

post.delete()
user.has_perm('myapp.view_post', post)
# False, because the post does not exist, but the pemission on the post is a weak pointer
# So it still exist on table: "guardian_userobjectpermission" and "guardian_groupobjectpermission"
# content_type_id refere to the table, object_id the weak pointer to the object of that table
"""
