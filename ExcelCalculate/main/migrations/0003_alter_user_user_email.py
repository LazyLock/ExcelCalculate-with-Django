# Generated by Django 4.0 on 2021-12-16 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_user_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
