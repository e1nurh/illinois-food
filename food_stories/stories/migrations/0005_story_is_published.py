# Generated by Django 4.1.7 on 2023-05-02 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0004_alter_story_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='story',
            name='is_published',
            field=models.BooleanField(default=False),
        ),
    ]
