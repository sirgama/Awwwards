# Generated by Django 4.0.5 on 2022-06-13 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='site',
            name='category',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
