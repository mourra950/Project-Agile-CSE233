# Generated by Django 4.1.3 on 2022-12-24 12:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Asec', '0003_rename_commitee_committee_des'),
    ]

    operations = [
        migrations.CreateModel(
            name='Committee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=255)),
                ('photo', models.CharField(max_length=30)),
                ('head', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='committee', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
