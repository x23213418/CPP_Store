# Generated by Django 4.2.3 on 2024-04-15 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.TextField(default='dfwfw'),
        ),
        migrations.AlterField(
            model_name='order',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]