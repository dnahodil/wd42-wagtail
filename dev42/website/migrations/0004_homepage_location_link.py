# Generated by Django 2.0.5 on 2018-05-24 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_add_location_fields'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='location_link',
            field=models.URLField(default='https://goo.gl/maps/5UE2BXbGzq52', help_text='Link to a map of the event location'),
            preserve_default=False,
        ),
    ]