# Generated by Django 3.2.4 on 2021-06-30 11:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_alter_product_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='comments',
            new_name='comment',
        ),
    ]
