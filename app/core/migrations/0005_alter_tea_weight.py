# Generated by Django 3.2.18 on 2023-05-03 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20230503_1436'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tea',
            name='weight',
            field=models.CharField(blank=True, choices=[('50', '50'), ('100', '100'), ('200', '200'), ('250', '250'), ('500', '500'), ('1000', '1000')], max_length=250, null=True, verbose_name='Çəkisi'),
        ),
    ]
