# Generated by Django 3.2.5 on 2021-07-23 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GateWay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=150, null=True, unique=True, verbose_name='网关名称')),
                ('topic', models.CharField(blank=True, max_length=150, null=True, unique=True, verbose_name='网关主题')),
                ('gateway_id', models.CharField(blank=True, max_length=150, null=True, unique=True, verbose_name='网关ID')),
                ('location', models.CharField(blank=True, max_length=150, null=True, unique=True, verbose_name='网关位置')),
            ],
            options={
                'db_table': 'app_gateway',
            },
        ),
    ]
