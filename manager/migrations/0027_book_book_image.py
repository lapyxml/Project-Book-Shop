# Generated by Django 3.1.3 on 2020-12-30 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0026_auto_20201230_1430'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='book_image',
            field=models.ImageField(blank=True, null=True, upload_to='manager/'),
        ),
    ]