# Generated by Django 2.2.5 on 2019-09-10 08:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_post_title'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Post',
        ),
    ]
