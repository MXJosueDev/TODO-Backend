# Generated by Django 5.1 on 2024-08-21 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_alter_list_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
