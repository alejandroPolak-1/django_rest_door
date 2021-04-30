# Generated by Django 3.2 on 2021-04-30 12:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Door',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('hash', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Personal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('lastname', models.CharField(max_length=255)),
                ('dni', models.CharField(max_length=30)),
                ('movil_user', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='PersonalByDoors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('door', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_movil.door')),
                ('personal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_movil.personal')),
            ],
            options={
                'unique_together': {('personal', 'door')},
            },
        ),
        migrations.AddField(
            model_name='personal',
            name='doors',
            field=models.ManyToManyField(through='api_movil.PersonalByDoors', to='api_movil.Door'),
        ),
        migrations.AddField(
            model_name='door',
            name='personals',
            field=models.ManyToManyField(through='api_movil.PersonalByDoors', to='api_movil.Personal'),
        ),
    ]