# Generated by Django 2.2.3 on 2020-07-22 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='publication_year',
            field=models.DateField(),
        ),
    ]