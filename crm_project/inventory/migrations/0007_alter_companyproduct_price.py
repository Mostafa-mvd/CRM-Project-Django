# Generated by Django 3.2.5 on 2021-07-30 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0006_alter_companyproduct_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companyproduct',
            name='price',
            field=models.PositiveIntegerField(default=0, verbose_name='قیمت'),
        ),
    ]