# Generated by Django 3.2.7 on 2021-11-14 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('csit', '0003_notefile_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='notefile',
            name='name',
            field=models.CharField(max_length=80, null=True),
        ),
    ]
