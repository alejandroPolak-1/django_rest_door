# Generated by Django 3.2 on 2021-04-30 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_movil', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='door',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]