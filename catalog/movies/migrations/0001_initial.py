# Generated by Django 4.1 on 2022-09-12 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.CharField(max_length=50)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
