# Generated by Django 5.0.4 on 2024-05-02 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapp', '0002_alter_customer_address_alter_customer_date_of_birth_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='date_of_birth',
            field=models.DateField(),
        ),
    ]