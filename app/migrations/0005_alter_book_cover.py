# Generated by Django 3.2.12 on 2023-07-04 10:33

from django.db import migrations
import versatileimagefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20230704_1030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='cover',
            field=versatileimagefield.fields.VersatileImageField(blank=True, null=True, upload_to='customers/', verbose_name='Book Cover'),
        ),
    ]
