# Generated by Django 4.1.1 on 2023-09-06 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0004_job_company_address_job_company_country_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='company_size',
            field=models.CharField(choices=[('size_1_9', '1_9'), ('size_10_49', '10_49'), ('size_50_99', '50_99'), ('size_100', '100+')], default='size_1_9', max_length=20),
        ),
    ]