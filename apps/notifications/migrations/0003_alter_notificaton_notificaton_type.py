# Generated by Django 4.1.1 on 2023-09-01 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0002_alter_notificaton_notificaton_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notificaton',
            name='Notificaton_type',
            field=models.TextField(choices=[('message', 'message'), ('application', 'application')], max_length=28),
        ),
    ]
