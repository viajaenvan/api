# Generated by Django 2.1.7 on 2019-05-28 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='model',
            name='year',
            field=models.IntegerField(choices=[('1980', '1980'), ('1981', '1980')], default=2000),
            preserve_default=False,
        ),
    ]
