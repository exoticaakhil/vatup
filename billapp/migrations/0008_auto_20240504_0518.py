# Generated by Django 3.2.25 on 2024-05-04 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billapp', '0007_auto_20240503_1121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='debitnote',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='debitnote',
            name='grandtotal',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, null=True),
        ),
    ]
