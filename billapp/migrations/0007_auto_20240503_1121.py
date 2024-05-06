# Generated by Django 3.2.25 on 2024-05-03 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billapp', '0006_alter_transactions_party_party'),
    ]

    operations = [
        migrations.AlterField(
            model_name='debitnote',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='debitnote',
            name='grandtotal',
            field=models.FloatField(default=0, null=True),
        ),
    ]
