# Generated by Django 3.1.1 on 2020-09-10 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productscategory',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
