# Generated by Django 4.0.5 on 2022-06-13 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_alter_rating_content_alter_rating_design_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='content',
            field=models.CharField(blank=True, max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='rating',
            name='design',
            field=models.CharField(blank=True, max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='rating',
            name='usability',
            field=models.CharField(blank=True, max_length=2, null=True),
        ),
    ]