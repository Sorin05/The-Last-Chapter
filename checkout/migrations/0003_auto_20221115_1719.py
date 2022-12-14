# Generated by Django 3.2 on 2022-11-15 17:19

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_auto_20221111_1753'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='post_code',
        ),
        migrations.AddField(
            model_name='order',
            name='original_bag',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='order',
            name='postcode',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='stripe_pid',
            field=models.CharField(default='', max_length=254),
        ),
        migrations.AddField(
            model_name='orderlineitem',
            name='lineitem_total',
            field=models.DecimalField(decimal_places=2, editable=False, max_digits=6, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='country',
            field=django_countries.fields.CountryField(max_length=2),
        ),
        migrations.AlterField(
            model_name='order',
            name='county',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='street_address2',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='town_or_city',
            field=models.CharField(max_length=40),
        ),
    ]
