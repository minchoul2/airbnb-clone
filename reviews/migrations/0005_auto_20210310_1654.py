# Generated by Django 2.2.5 on 2021-03-10 07:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0004_auto_20210310_1642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='rooms.Room'),
        ),
    ]
