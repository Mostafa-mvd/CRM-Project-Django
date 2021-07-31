# Generated by Django 3.2.5 on 2021-07-31 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketing', '0007_followup_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quoteitem',
            name='discount',
            field=models.FloatField(default=0.0, verbose_name='درصد تخفیف'),
        ),
        migrations.AlterField(
            model_name='quoteitem',
            name='price',
            field=models.PositiveIntegerField(default=0, verbose_name='قیمت کل'),
        ),
    ]
