# Generated by Django 3.2.18 on 2023-05-03 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20230503_0022'),
    ]

    operations = [
        migrations.AddField(
            model_name='tea',
            name='new_arrival',
            field=models.BooleanField(default=False, verbose_name='Yeni gələn'),
        ),
        migrations.AddField(
            model_name='tea',
            name='premium',
            field=models.BooleanField(default=False, verbose_name='Premium'),
        ),
        migrations.AddField(
            model_name='tea',
            name='stock_quantity',
            field=models.IntegerField(blank=True, null=True, verbose_name='Stok sayı'),
        ),
        migrations.AlterField(
            model_name='tea',
            name='weight',
            field=models.DecimalField(blank=True, choices=[('50', '50'), ('100', '100'), ('200', '200'), ('250', '250'), ('500', '500'), ('1000', '1000')], decimal_places=2, max_digits=5, null=True, verbose_name='Çəkisi'),
        ),
    ]
