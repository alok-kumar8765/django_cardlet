# Generated by Django 4.1.1 on 2022-10-10 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newset', '0002_flashcard_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='set',
            name='set_id',
            field=models.IntegerField(unique=True),
        ),
    ]