# Generated by Django 2.2.5 on 2019-09-26 12:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_post_creator'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='niceplace',
            name='country',
        ),
        migrations.DeleteModel(
            name='Country',
        ),
        migrations.DeleteModel(
            name='NicePlace',
        ),
    ]
