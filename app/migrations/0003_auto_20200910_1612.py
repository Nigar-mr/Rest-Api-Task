# Generated by Django 3.1.1 on 2020-09-10 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20200910_1447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productscategory',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterUniqueTogether(
            name='productscategory',
            unique_together={('name',)},
        ),
    ]