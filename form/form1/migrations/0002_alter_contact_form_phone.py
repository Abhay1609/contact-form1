# Generated by Django 4.1.2 on 2023-01-06 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact_form',
            name='phone',
            field=models.IntegerField(),
        ),
    ]