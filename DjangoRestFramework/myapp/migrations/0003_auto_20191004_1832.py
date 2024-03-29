# Generated by Django 2.2.5 on 2019-10-04 18:32

from django.db import migrations


def create_post_group_permissions(apps, schema_editor):
    """create groups and assign them Post CRUD permissions"""
    Group = apps.get_model('auth', 'Group')
    groups = [Group.objects.create(name=name) for name in ['viewers', 'posters', 'editors']]

    ContentType = apps.get_model('contenttypes', 'ContentType')
    Post = apps.get_model('myapp', 'Post')

    content_type = ContentType.objects.get_for_model(Post)

    for index, codename in enumerate(['view_post', 'add_post', 'change_post']):
        groups[index].permissions.add(content_type.permission_set.filter(codename=codename).get())

    groups[2].permissions.add(content_type.permission_set.filter(codename='delete_post').get())


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20191004_1636'),
    ]

    operations = [
        migrations.RunPython(create_post_group_permissions)
    ]
