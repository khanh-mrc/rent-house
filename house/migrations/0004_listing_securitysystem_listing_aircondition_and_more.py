# Generated by Django 4.1.3 on 2022-12-02 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0003_remove_listing_area_remove_listing_badrooms_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='SecuritySystem',
            field=models.BooleanField(blank=True, default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='listing',
            name='aircondition',
            field=models.BooleanField(blank=True, default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='listing',
            name='area',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='listing',
            name='bathrooms',
            field=models.IntegerField(blank=True, default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='listing',
            name='bedrooms',
            field=models.IntegerField(blank=True, default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='listing',
            name='kitcheen',
            field=models.IntegerField(blank=True, default=0),
            preserve_default=False,
        ),
    ]
