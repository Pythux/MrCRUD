# Generated by Django 2.2.5 on 2019-09-17 17:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20190917_1601'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='country',
            name='niceplace',
        ),
        migrations.AddField(
            model_name='niceplace',
            name='country',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='myapp.Country'),
            preserve_default=False,
        ),
    ]