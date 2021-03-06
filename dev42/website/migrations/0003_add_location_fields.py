# Generated by Django 2.0.5 on 2018-05-23 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_django_2_0_changes'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='location_lat',
            field=models.DecimalField(decimal_places=7, default=-42.885563, max_digits=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='homepage',
            name='location_lng',
            field=models.DecimalField(decimal_places=7, default=147.326996, max_digits=10),
            preserve_default=False,
        ),
    ]
