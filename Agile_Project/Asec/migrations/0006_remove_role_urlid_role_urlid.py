# Generated by Django 4.1.3 on 2022-12-27 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Asec', '0005_urls_remove_committee_head_committee_headid_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='role',
            name='urlId',
        ),
        migrations.AddField(
            model_name='role',
            name='urlId',
            field=models.ManyToManyField(to='Asec.urls'),
        ),
    ]
