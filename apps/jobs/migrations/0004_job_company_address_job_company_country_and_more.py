# Generated by Django 4.1.1 on 2023-09-02 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0003_application'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='company_address',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='company_country',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='company_name',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='job',
            name='company_place',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='company_size',
            field=models.CharField(choices=[('size_1_9', '1_9'), ('size_10_49', '10_49'), ('size_59_99', '59_99'), ('size_100', '100+')], default='size_1_9', max_length=20),
        ),
        migrations.AddField(
            model_name='job',
            name='company_zipcode',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
