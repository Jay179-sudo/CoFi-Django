# Generated by Django 4.0.8 on 2023-02-05 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transactions',
            name='Transaction_Date',
            field=models.DateField(),
        ),
    ]