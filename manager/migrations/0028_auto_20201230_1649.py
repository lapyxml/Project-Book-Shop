# Generated by Django 3.1.3 on 2020-12-30 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0027_book_book_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genre',
            name='text',
            field=models.TextField(db_index=True),
        ),
    ]