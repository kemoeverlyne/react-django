# Generated by Django 2.0.7 on 2021-04-06 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='description',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
